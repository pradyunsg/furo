"""A clean customizable Sphinx documentation theme."""

__version__ = "0.1.0.dev0"

from pathlib import Path

from .navigation import get_navigation_tree


def sphinx_html_page_context(app, pagename, templatename, context, doctree):
    """Handler for Sphinx's `html-page-context` event."""

    # Custom Navigation Tree (adds checkboxes and labels)
    toctree = context.get("toctree", lambda **kwargs: "")
    toctree_html = toctree(
        collapse=False, titles_only=True, maxdepth=-1, includehidden=True
    )
    context["mawek_navigation_tree"] = get_navigation_tree(toctree_html)


def setup(app):
    """Entry point for sphinx theming."""
    theme_path = (Path(__file__).parent / "templates").resolve()
    app.add_html_theme("mawek", str(theme_path))

    app.connect("html-page-context", sphinx_html_page_context)
