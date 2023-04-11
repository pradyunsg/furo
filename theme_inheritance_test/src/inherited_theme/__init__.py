"""A bare-bones theme that inherits Furo to test that inheritance works."""

from functools import partial
from pathlib import Path
from typing import Any, Dict

import sphinx.application

from furo import (
    WrapTableAndMathInAContainerTransform,
    _builder_inited,
    _html_page_context,
    _overwrite_pygments_css,
)


def setup(app: sphinx.application.Sphinx) -> Dict[str, Any]:
    """Entry point for Sphinx theming."""
    app.add_html_theme(
        "inherited_theme",
        (Path(__file__).parent / "theme" / "inherited_theme").resolve(),
    )

    # All the below must be kept in sync with `furo/__init__.py`. We use `partial` to turn off
    # validation that the theme is "furo".
    page_context = partial(_html_page_context, validate_furo=False)
    builder_init = partial(_builder_inited, validate_furo=False)

    app.add_post_transform(WrapTableAndMathInAContainerTransform)

    app.connect("html-page-context", page_context)
    app.connect("builder-inited", builder_init)
    app.connect("build-finished", _overwrite_pygments_css)
    return {"parallel_read_safe": True, "parallel_write_safe": True}
