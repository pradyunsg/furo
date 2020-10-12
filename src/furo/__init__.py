"""A clean customisable Sphinx documentation theme."""

__version__ = "2020.10.13.beta10"

import secrets
from pathlib import Path

from .body import wrap_elements_that_can_get_too_wide
from .code import get_pygments_style_colors
from .navigation import get_navigation_tree
from .toc import should_hide_toc


def _get_colors_for_codeblocks(highlighter, *, fg, bg):
    return get_pygments_style_colors(
        highlighter.formatter_args["style"],
        fallbacks={"foreground": fg, "background": bg},
    )


def _html_page_context(app, pagename, templatename, context, doctree):
    if app.config.html_theme != "furo":
        return

    # Custom Navigation Tree (adds checkboxes and labels)
    toctree = context.get("toctree", lambda **kwargs: "")
    toctree_html = toctree(
        collapse=False, titles_only=True, maxdepth=-1, includehidden=True
    )
    context["furo_navigation_tree"] = get_navigation_tree(toctree_html)

    # Custom "should hide ToC" logic
    context["furo_hide_toc"] = should_hide_toc(context.get("toc", ""))
    # Allow for hiding toc via ToC in page-wide metadata.
    if "hide-toc" in (context.get("meta", None) or {}):
        context["furo_hide_toc"] = True

    # Inject information about styles
    context["furo_pygments"] = {
        "light": _get_colors_for_codeblocks(
            app.builder.highlighter,
            fg="black",
            bg="white",
        ),
        "dark": _get_colors_for_codeblocks(
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
