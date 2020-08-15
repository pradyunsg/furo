"""I still have to figure out what this would be."""

__version__ = "0.1.0.dev0"

from pathlib import Path

from .navigation import get_navigation_tree


def add_navigation_tree_to(context):
    toctree = context["toctree"]
    toctree_html = toctree(
        collapse=False, titles_only=True, maxdepth=-1, includehidden=True
    )

    context["mawek_navigation_tree"] = get_navigation_tree(toctree_html)


def sphinx_html_page_context(app, pagename, templatename, context, doctree):
    add_navigation_tree_to(context)


def setup(app):
    """Entry point for sphinx theming."""
    theme_path = (Path(__file__).parent / "templates").resolve()
    app.add_html_theme("mawek", str(theme_path))

    app.connect("html-page-context", sphinx_html_page_context)
