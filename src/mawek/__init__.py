"""I still have to figure out what this would be."""

__version__ = "0.1.0.dev0"

from pathlib import Path

theme_path = (Path(__file__).parent / "templates").resolve()


def setup(app):
    """Entry point for sphinx theming."""
    app.add_html_theme("mawek", str(theme_path))
