"""Generate the navigation tree from Sphinx's toctree function's output."""

import functools
import re

from bs4 import BeautifulSoup, Tag


def _get_navigation_expand_image(soup: BeautifulSoup) -> Tag:
    retval = soup.new_tag("i", attrs={"class": "icon"})

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

        # Add the "label" for the checkbox which will get filled.
        label = soup.new_tag("label", attrs={"for": checkbox_name})
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
            },
        )
        # if this has a "current" class, be expanded by default (by checking the checkbox)
        if "current" in classes:
            checkbox.attrs["checked"] = ""

        element.insert(1, checkbox)

    # replaces toc text that follows sphinx_fontawesome substitution rules:
    # https://github.com/fraoustin/sphinx_fontawesome
    for element in soup.find_all("li", {"class": "toctree-l1"}, recursive=True):
        match = re.match("\|([a-z-]+)\| ", element.text)
        new_text = re.sub("\|[a-z-]+\| ", "", element.text)
        if match:
            fa_tag = soup.new_tag("i", attrs={"class": f"fa fa-{match.group(1)}"})
            link = element.find("a")
            link.string = new_text
            link.insert(0, fa_tag)

    if last_element_with_current is not None:
        last_element_with_current["class"].append("current-page")

    return str(soup)
