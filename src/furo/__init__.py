"""A clean customizable Sphinx documentation theme."""

__version__ = "2020.9.8.beta2"

from pathlib import Path

from .body import wrap_tables
from .code import get_pygments_style_colors
from .navigation import get_navigation_tree
from .toc import should_hide_toc


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
    colors = get_pygments_style_colors(
        app.builder.highlighter.formatter_args["style"],
        fallbacks={"foreground": "#000000", "background": "#FFFFFF"},
    )
    context["furo_pygments"] = colors

    # Patch the content
    if "body" in context:
        context["body"] = wrap_tables(context["body"])


def setup(app):
    """Entry point for sphinx theming."""
    theme_path = (Path(__file__).parent / "theme").resolve()
    app.add_html_theme("furo", str(theme_path))

    app.connect("html-page-context", _html_page_context)
