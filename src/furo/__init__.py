"""A clean customisable Sphinx documentation theme."""

__version__ = "2020.12.09.dev22"

import hashlib
from functools import lru_cache
from pathlib import Path

from bs4 import BeautifulSoup
from pygments.token import Text
from sphinx.builders.html import JavaScript

from .navigation import get_navigation_tree


@lru_cache(maxsize=None)
def has_exactly_one_list_item(toc):
    """Check if the toc has exactly one list item."""
    assert toc

    soup = BeautifulSoup(toc, "html.parser")
    if len(soup.find_all("li")) == 1:
        return True

    return False


def wrap_elements_that_can_get_too_wide(content):
    """Wrap the elements that could get too wide, with a div to allow controlling width.

    - <table>
    - [class=math]

    """
    soup = BeautifulSoup(content, "html.parser")

    for table in soup.find_all("table"):
        table_wrapper = soup.new_tag("div", attrs={"class": "table-wrapper"})
        table.replace_with(table_wrapper)
        table_wrapper.append(table)

    for math in soup.find_all("div", class_="math"):
        wrapper = soup.new_tag("div", attrs={"class": "math-wrapper"})
        math.replace_with(wrapper)
        wrapper.append(math)

    return str(soup)


def get_pygments_style_colors(style, *, fallbacks):
    """Get background/foreground colors for given pygments style."""
    background = style.background_color
    text_colors = style.style_for_token(Text)
    foreground = text_colors["color"]

    if not background:
        background = fallbacks["background"]

    if not foreground:
        foreground = fallbacks["foreground"]
    else:
        foreground = f"#{foreground}"

    return {"background": background, "foreground": foreground}


@lru_cache(maxsize=2)
def get_colors_for_codeblocks(highlighter, *, fg, bg):
    """Get background/foreground colors for given pygments style."""
    return get_pygments_style_colors(
        highlighter.formatter_args["style"],
        fallbacks={
            "foreground": fg,
            "background": bg,
        },
    )


def _compute_navigation_tree(context):
    # The navigation tree, generated from the sphinx-provided ToC tree.
    if "toctree" in context:
        toctree = context["toctree"]
        toctree_html = toctree(
            collapse=False,
            titles_only=True,
            maxdepth=-1,
            includehidden=True,
        )
    else:
        toctree_html = ""

    return get_navigation_tree(toctree_html)


def _compute_hide_toc(context):
    # Should the table of contents be hidden?
    file_meta = context.get("meta", None) or {}
    if "hide-toc" in file_meta:
        return True
    elif "toc" not in context:
        return True
    elif not context["toc"]:
        return True

    return has_exactly_one_list_item(context["toc"])


@lru_cache(maxsize=None)
def furo_asset_hash(path):
    """Append a `?digest=` to an url based on the file content."""
    _static = "_static/"
    if _static not in path:
        raise ValueError("furo_asset_hash expect a path with '_static' in it")

    partial_path = path[path.find(_static) + len(_static) :]

    file_path = Path(__file__).parent / "theme/static" / partial_path
    with open(file_path, "rb") as f:
        digest = hashlib.sha1(f.read()).hexdigest()

    return path + f"?digest={digest}"


def _html_page_context(app, pagename, templatename, context, doctree):
    if app.config.html_theme != "furo":
        return

    # Add attributes to the scripts loaded with `js_tag`
    sphinx_js_tag = context["js_tag"]

    def furo_js_tag(js):
        if isinstance(js, JavaScript):
            js.attributes["defer"] = "defer"
        return sphinx_js_tag(js)

    context["js_tag"] = furo_js_tag

    # Basic constants
    context["furo_version"] = __version__
    context["furo_asset_hash"] = furo_asset_hash

    # Values computed from page-level context.
    context["furo_navigation_tree"] = _compute_navigation_tree(context)
    context["furo_hide_toc"] = _compute_hide_toc(context)

    # Inject information about styles
    context["furo_pygments"] = {
        "light": get_colors_for_codeblocks(
            app.builder.highlighter,
            fg="black",
            bg="white",
        ),
        "dark": get_colors_for_codeblocks(
            app.builder.dark_highlighter,
            fg="white",
            bg="black",
        ),
    }

    # Patch the content
    if "body" in context:
        context["body"] = wrap_elements_that_can_get_too_wide(context["body"])


def setup(app):
    """Entry point for sphinx theming."""
    app.require_sphinx("3.0")

    theme_path = (Path(__file__).parent / "theme").resolve()
    app.add_html_theme("furo", str(theme_path))

    app.connect("html-page-context", _html_page_context)

    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
        "version": __version__,
    }
