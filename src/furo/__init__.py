"""A clean customisable Sphinx documentation theme."""

__version__ = "2021.02.28.beta28"

import hashlib
from functools import lru_cache
from pathlib import Path
from typing import Any, Dict

import pygments
import sphinx
from bs4 import BeautifulSoup
from sphinx.highlighting import PygmentsBridge

from .navigation import get_navigation_tree

THEME_PATH = (Path(__file__).parent / "theme" / "furo").resolve()


@lru_cache(maxsize=None)
def has_exactly_one_list_item(toc: str) -> bool:
    """Check if the toc has exactly one list item."""
    assert toc

    soup = BeautifulSoup(toc, "html.parser")
    if len(soup.find_all("li")) == 1:
        return True

    return False


def wrap_elements_that_can_get_too_wide(content: str) -> str:
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


def get_pygments_style_colors(
    style: pygments.style.Style, *, fallbacks: Dict[str, str]
) -> Dict[str, str]:
    """Get background/foreground colors for given pygments style."""
    background = style.background_color
    text_colors = style.style_for_token(pygments.token.Text)
    foreground = text_colors["color"]

    if not background:
        background = fallbacks["background"]

    if not foreground:
        foreground = fallbacks["foreground"]
    else:
        foreground = f"#{foreground}"

    return {"background": background, "foreground": foreground}


@lru_cache(maxsize=2)
def get_colors_for_codeblocks(
    highlighter: PygmentsBridge, *, fg: str, bg: str
) -> Dict[str, str]:
    """Get background/foreground colors for given pygments style."""
    return get_pygments_style_colors(
        highlighter.formatter_args["style"],
        fallbacks={
            "foreground": fg,
            "background": bg,
        },
    )


def _compute_navigation_tree(context: Dict[str, Any]) -> str:
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


def _compute_hide_toc(context: Dict[str, Any]) -> bool:
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
def furo_asset_hash(path: str) -> str:
    """Append a `?digest=` to an url based on the file content."""
    full_path = THEME_PATH / "static" / path
    digest = hashlib.sha1(full_path.read_bytes()).hexdigest()

    return f"_static/{path}?digest={digest}"


def _html_page_context(
    app: sphinx.application.Sphinx,
    pagename: str,
    templatename: str,
    context: Dict[str, Any],
    doctree: Any,
) -> None:
    if app.config.html_theme != "furo":
        return

    # Basic constants
    context["furo_version"] = __version__

    # Assets
    context["furo_assets"] = {
        "furo-extensions.css": furo_asset_hash("styles/furo-extensions.css"),
        "main.js": furo_asset_hash("scripts/main.js"),
    }

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

    should_use_own_styles = (
        # Not using the HTML builders with Furo for some reason?
        "style" not in context
        # Did not override Furo's default CSS
        or context["style"] == "styles/furo.css"
    )
    if should_use_own_styles:
        context["furo_assets"]["style"] = furo_asset_hash("styles/furo.css")
    else:
        context["furo_assets"]["style"] = "_static/" + context["style"]


def _builder_inited(app: sphinx.application.Sphinx) -> None:
    if app.config.html_theme != "furo":
        return

    builder = app.builder
    assert builder.dark_highlighter is None, "this shouldn't happen."
    builder.dark_highlighter = PygmentsBridge("html", app.config.pygments_dark_style)


def setup(app: sphinx.application.Sphinx) -> Dict[str, Any]:
    """Entry point for sphinx theming."""
    app.require_sphinx("3.0")

    app.add_config_value("pygments_dark_style", "native", "env", [str])

    app.add_html_theme("furo", str(THEME_PATH))

    app.connect("html-page-context", _html_page_context)
    app.connect("builder-inited", _builder_inited)

    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
        "version": __version__,
    }
