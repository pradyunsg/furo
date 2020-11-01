"""A clean customisable Sphinx documentation theme."""

__version__ = "2020.11.01.dev15"

import secrets
from functools import lru_cache
from pathlib import Path

from bs4 import BeautifulSoup
from pygments.token import Text

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


def get_colors_for_codeblocks(highlighter, *, fg, bg):
    """Get background/foreground colors for given pygments style."""
    return get_pygments_style_colors(
        highlighter.formatter_args["style"],
        fallbacks={"foreground": fg, "background": bg},
    )


def _html_page_context(app, pagename, templatename, context, doctree):
    if app.config.html_theme != "furo":
        return

    # Custom Navigation Tree (adds checkboxes and labels)
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

    context["furo_navigation_tree"] = get_navigation_tree(toctree_html)

    # Should the table of contents be hidden?
    if "hide-toc" in context.get("meta", {}):
        context["furo_hide_toc"] = True
    elif "toc" not in context:
        context["furo_hide_toc"] = True
    elif not context["toc"]:
        context["furo_hide_toc"] = True
    else:
        context["furo_hide_toc"] = has_exactly_one_list_item(context["toc"])

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

    context["furo_version"] = __version__

    # Include a hash to ensure the assets get refreshed.
    context["furo_asset_hash"] = secrets.token_hex(12)


def setup(app):
    """Entry point for sphinx theming."""
    app.require_sphinx("3.0")

    theme_path = (Path(__file__).parent / "theme").resolve()
    app.add_html_theme("furo", str(theme_path))

    app.connect("html-page-context", _html_page_context)
