"""Generate and cache Furo's navigation tree.

Furo starts from the HTML fragment produced by Sphinx's toctree machinery.
``get_navigation_tree`` performs the traditional one-time Furo augmentation on
that fragment: it adds the CSS-only collapse controls, marks entries that have
children, and preserves the same current-page class behavior as the original
BeautifulSoup-based implementation.

``_NavigationTree`` is the cacheable second phase.  It compiles the augmented
HTML into a much smaller tree of constants and ``_NavigationElement`` objects.
That reduced tree is not a general-purpose DOM.  It retains only the information
that changes between pages: link targets, ancestor membership for current-state
classes, the list item representing each page, and the checkbox associated with
each expandable branch.  Rendering a page then patches those pieces directly
instead of asking Sphinx to resolve the global toctree and asking BeautifulSoup
to parse the full navigation HTML again.
"""

import functools
import html
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Set, Tuple

from bs4 import BeautifulSoup, Comment, NavigableString, Tag

_VOID_ELEMENTS = frozenset(
    {
        "area",
        "base",
        "br",
        "col",
        "embed",
        "hr",
        "img",
        "input",
        "link",
        "meta",
        "param",
        "source",
        "track",
        "wbr",
    }
)


def _get_navigation_expand_image(soup: BeautifulSoup) -> Tag:
    retval = soup.new_tag("span", attrs={"class": "icon"})

    svg_element = soup.new_tag("svg")
    svg_use_element = soup.new_tag("use", href="#svg-arrow-right")
    svg_element.append(svg_use_element)

    retval.append(svg_element)
    return retval


@functools.lru_cache(maxsize=None)
def get_navigation_tree(toctree_html: str) -> str:
    """Modify the given navigation tree, with furo-specific elements.

    Adds a checkbox + corresponding label to <li>s that contain a <ul> tag, to enable
    the I-spent-too-much-time-making-this-CSS-only collapsing sidebar tree.
    """
    if not toctree_html:
        return toctree_html

    soup = BeautifulSoup(toctree_html, "html.parser")

    toctree_checkbox_count = 0
    last_element_with_current = None
    for element in soup.find_all("li", recursive=True):
        # We check all "li" elements, to add a "current-page" to the correct li.
        classes = element.get("class", [])
        if "current" in classes:
            last_element_with_current = element

        # Nothing more to do, unless this has "children"
        if not element.find("ul"):
            continue

        # Add a class to indicate that this has children.
        element["class"] = classes + ["has-children"]

        # We're gonna add a checkbox.
        toctree_checkbox_count += 1
        checkbox_name = f"toctree-checkbox-{toctree_checkbox_count}"
        accessible_name = f"Toggle navigation of {element.find('a').text}"

        # Add the "label" for the checkbox which will get filled.
        label = soup.new_tag(
            "label",
            attrs={
                "for": checkbox_name,
            },
        )
        label.append(_get_navigation_expand_image(soup))

        element.insert(1, label)

        # Add the checkbox that's used to store expanded/collapsed state.
        checkbox = soup.new_tag(
            "input",
            attrs={
                "type": "checkbox",
                "class": ["toctree-checkbox"],
                "id": checkbox_name,
                "name": checkbox_name,
                "role": "switch",
                "aria-label": accessible_name,
            },
        )
        # if this has a "current" class, be expanded by default (by checking the checkbox)
        if "current" in classes:
            checkbox.attrs["checked"] = ""

        element.insert(1, checkbox)

    if last_element_with_current is not None:
        last_element_with_current["class"].append("current-page")

    return str(soup)


def _as_class_list(value: Any) -> List[str]:
    if value is None:
        return []
    if isinstance(value, str):
        return value.split()
    return [str(item) for item in value]


def _stringify_attribute_value(value: Any) -> str:
    if isinstance(value, list):
        return " ".join(str(item) for item in value)
    return str(value)


def _add_current_class(classes: List[str], *, tag: str) -> None:
    if "current" in classes:
        return
    if tag == "a":
        classes.insert(0, "current")
        return
    try:
        index = classes.index("has-children")
    except ValueError:
        classes.append("current")
    else:
        classes.insert(index, "current")


def _find_target(
    href: str, token_to_docname: Dict[str, str]
) -> Tuple[Optional[str], str]:
    for token, docname in token_to_docname.items():
        if href == token:
            return docname, ""
        if href.startswith(token + "#"):
            return docname, href[len(token) :]
    return None, ""


def _render_attributes(attrs: Dict[str, str]) -> str:
    if not attrs:
        return ""

    rendered = []
    for name in sorted(attrs):
        value = attrs[name]
        rendered.append(f'{name}="{html.escape(value, quote=True)}"')
    return " " + " ".join(rendered)


@dataclass
class _NavigationElement:
    """A reduced HTML element used to render cached navigation HTML.

    Instances form a tree with string children for already-rendered text and
    comments.  They intentionally model only the subset of HTML that Furo needs
    to vary per page:

    * ``target_docname`` and ``target_anchor`` describe an ``<a href>`` whose
      canonical placeholder link must be replaced with a page-relative link.
    * ``current_docnames`` is the set of pages contained by this element's
      subtree; ``<li>`` and ``<ul>`` elements use it to regain the ``current``
      class for the active branch.
    * ``checkbox_docnames`` is set on Furo's ``<input class="toctree-checkbox">``
      controls so the current branch can be expanded with ``checked=""``.
    * ``current_page_index`` identifies the list item that should receive
      ``current-page`` for a given docname.

    The result is a partially parsed navigation tree: enough structure to patch
    ``href``, ``class``, and ``checked`` attributes deterministically, without
    carrying the cost and API surface of a full BeautifulSoup tree.
    """

    name: str
    attrs: Dict[str, str]
    children: List[Any]
    target_docname: Optional[str] = None
    target_anchor: str = ""
    current_docnames: Set[str] = field(default_factory=set)
    checkbox_docnames: Set[str] = field(default_factory=set)
    current_page_index: Optional[int] = None

    @property
    def _is_current_page_link(self) -> bool:
        return (
            self.name == "a"
            and self.target_docname is not None
            and not self.target_anchor
        )

    def render(
        self,
        *,
        builder: Any,
        pagename: str,
        current_page_index: Optional[int],
    ) -> str:
        attrs = dict(self.attrs)

        # All per-page class updates happen on a copy of the cached attributes.
        # The cached tree must remain canonical so the next page starts from the
        # same state.
        classes = _as_class_list(attrs.get("class"))

        # Sphinx marks every ancestor of the current page with "current".  The
        # cached tree was built with no page current, so restore that class from
        # the precomputed subtree docname set.
        if self.name in {"li", "ul"} and pagename in self.current_docnames:
            _add_current_class(classes, tag=self.name)

        # The <a> for the current document also carries "current".
        if self._is_current_page_link and self.target_docname == pagename:
            _add_current_class(classes, tag=self.name)

        # Furo additionally marks exactly one <li> as "current-page".  The
        # numeric index preserves BeautifulSoup-era behavior when a document is
        # linked more than once: the last matching list item wins.
        if (
            self.name == "li"
            and self.current_page_index is not None
            and self.current_page_index == current_page_index
        ):
            classes.append("current-page")
        if classes:
            attrs["class"] = " ".join(classes)
        else:
            attrs.pop("class", None)

        # Canonical links were captured as placeholder tokens so the tree could
        # be shared by every page.  Resolve them through the real builder here,
        # where the source page is known.  Sphinx renders a self-link as "", but
        # the browser needs "#" in an href.
        if self.target_docname is not None and "href" in attrs:
            attrs["href"] = (
                builder.get_relative_uri(pagename, self.target_docname)
                + self.target_anchor
            ) or "#"

        # Furo's left navigation opens branches with checkbox state.  Recompute
        # that state from the cached subtree membership instead of storing the
        # checked attribute from whichever page happened to build the cache.
        if self.name == "input" and "toctree-checkbox" in _as_class_list(
            self.attrs.get("class")
        ):
            if pagename in self.checkbox_docnames:
                attrs["checked"] = ""
            else:
                attrs.pop("checked", None)

        attributes = _render_attributes(attrs)
        if self.name in _VOID_ELEMENTS and not self.children:
            return f"<{self.name}{attributes}/>"

        rendered_children = "".join(
            child.render(
                builder=builder,
                pagename=pagename,
                current_page_index=current_page_index,
            )
            if isinstance(child, _NavigationElement)
            else child
            for child in self.children
        )
        return f"<{self.name}{attributes}>{rendered_children}</{self.name}>"


class _NavigationTree:
    """A cacheable representation of Furo's left navigation.

    The input HTML is the canonical navigation fragment produced by Sphinx and
    augmented by ``get_navigation_tree``.  During construction, it is converted
    into a tree of strings and ``_NavigationElement`` objects.  Text and comment
    nodes become pre-escaped strings.  Element nodes keep only the static
    attributes plus the small amount of dynamic state required to render any
    page:

    * placeholder ``href`` tokens mapped back to docnames and anchors,
    * descendant docname sets used to mark the current branch,
    * branch docname sets used to check expandable navigation inputs, and
    * the per-docname list-item index used for ``current-page``.

    Rendering is therefore linear in the navigation HTML size and does not
    invoke Sphinx's global toctree resolver or BeautifulSoup for each output
    page.
    """

    def __init__(self, html: str, *, token_to_docname: Dict[str, str]) -> None:
        self._current_page_indices: Dict[str, int] = {}
        self._next_current_page_index = 0

        soup = BeautifulSoup(html, "html.parser")
        self._children = [
            self._compile_node(child, token_to_docname) for child in soup.contents
        ]

    def _compile_node(self, node: Any, token_to_docname: Dict[str, str]) -> Any:
        # Preserve comments and escape text nodes up front.  BeautifulSoup does
        # this serialization work once here instead of once per output page.
        if isinstance(node, Comment):
            return f"<!--{node}-->"
        if isinstance(node, NavigableString):
            return html.escape(str(node), quote=False)
        if not isinstance(node, Tag):
            return ""

        attrs = {
            str(key): _stringify_attribute_value(value)
            for key, value in node.attrs.items()
        }

        target_docname = None
        target_anchor = ""
        if node.name == "a" and "href" in attrs:
            # Links in the canonical tree point at placeholder tokens generated
            # by _NavigationTreeBuilder.  Record the real target once, then
            # render page-relative hrefs later with the active Sphinx builder.
            target_docname, target_anchor = _find_target(
                attrs["href"], token_to_docname
            )

        children = [
            self._compile_node(child, token_to_docname) for child in node.contents
        ]

        current_docnames: Set[str] = set()
        if target_docname is not None and not target_anchor:
            current_docnames.add(target_docname)
        for child in children:
            if isinstance(child, _NavigationElement):
                current_docnames.update(child.current_docnames)

        # A list item's own page is normally the first page-level link under the
        # item, not necessarily the <li> itself.  Capturing this separately lets
        # render() apply "current-page" to the same element that the original
        # BeautifulSoup pass would have marked.
        current_page_docname = target_docname
        current_page_anchor = target_anchor
        if node.name == "li":
            for child in children:
                if (
                    isinstance(child, _NavigationElement)
                    and child._is_current_page_link
                ):
                    current_page_docname = child.target_docname
                    current_page_anchor = child.target_anchor
                    break

        current_page_index = None
        if (
            node.name == "li"
            and current_page_docname is not None
            and not current_page_anchor
        ):
            current_page_index = self._next_current_page_index
            self._next_current_page_index += 1
            # Match get_navigation_tree's "last element with current" behavior:
            # if a docname appears multiple times, the later <li> receives
            # "current-page".
            self._current_page_indices[current_page_docname] = current_page_index

        element = _NavigationElement(
            name=node.name,
            attrs=attrs,
            children=children,
            target_docname=target_docname,
            target_anchor=target_anchor,
            current_docnames=current_docnames,
            current_page_index=current_page_index,
        )

        if node.name == "li":
            # The checkbox Furo inserts for an expandable branch is a direct
            # child of that branch's <li>.  Attach the branch's docname set to
            # the checkbox so render() can add checked="" when the current page
            # is anywhere under that branch.
            for child in children:
                if (
                    isinstance(child, _NavigationElement)
                    and child.name == "input"
                    and "toctree-checkbox" in _as_class_list(child.attrs.get("class"))
                ):
                    child.checkbox_docnames = current_docnames

        return element

    def render(self, *, builder: Any, pagename: str) -> str:
        current_page_index = self._current_page_indices.get(pagename)
        return "".join(
            child.render(
                builder=builder,
                pagename=pagename,
                current_page_index=current_page_index,
            )
            if isinstance(child, _NavigationElement)
            else child
            for child in self._children
        )
