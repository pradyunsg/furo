"""A clean customisable Sphinx documentation theme."""

__version__ = "2025.12.19"

import hashlib
import logging
import os
from functools import lru_cache
from pathlib import Path
from typing import Any, Dict, Iterator, List, Optional, cast

import sphinx.application
from docutils import nodes
from pygments.formatters import HtmlFormatter
from pygments.style import Style
from pygments.token import Text
from sphinx.builders.dirhtml import DirectoryHTMLBuilder
from sphinx.builders.html import StandaloneHTMLBuilder
from sphinx.environment.adapters.toctree import TocTree
from sphinx.errors import ConfigError
from sphinx.highlighting import PygmentsBridge
from sphinx.transforms.post_transforms import SphinxPostTransform

from .navigation import get_navigation_tree

THEME_PATH = (Path(__file__).parent / "theme" / "furo").resolve()

logger = logging.getLogger(__name__)

# GLOBAL STATE
_KNOWN_STYLES_IN_USE: Dict[str, Optional[Style]] = {
    "light": None,
    "dark": None,
}


class WrapTableAndMathInAContainerTransform(SphinxPostTransform):
    """A Sphinx post-transform that wraps `table` and `div.math` in a container `div`.

    This makes it possible to handle these overflowing the content-width, which is
    necessary in a responsive theme.
    """

    formats = ("html",)
    default_priority = 500

    def run(self, **kwargs: Any) -> None:
        """Perform the post-transform on `self.document`."""
        get_nodes = (
            self.document.findall  # docutils 0.18+
            if hasattr(self.document, "findall")
            else self.document.traverse  # docutils <= 0.17.x
        )
        for table_node in list(get_nodes(nodes.table)):
            new_node = nodes.container(classes=["table-wrapper"])
            new_node.update_all_atts(table_node)
            table_node.parent.replace(table_node, new_node)
            new_node.append(table_node)

        for math_node in list(get_nodes(nodes.math_block)):
            new_node = nodes.container(classes=["math-wrapper"])
            new_node.update_all_atts(math_node)
            math_node.parent.replace(math_node, new_node)
            new_node.append(math_node)


def has_not_enough_items_to_show_toc(
    builder: StandaloneHTMLBuilder, docname: str
) -> bool:
    """Check if the toc has one or fewer items."""
    assert builder.env

    toctree = TocTree(builder.env).get_toc_for(docname, builder)
    try:
        self_toctree = toctree[0][1]  # type: ignore[index]
    except IndexError:
        val = True
    else:
        # There's only the page's own toctree(s) in there.
        val = all(entry.tagname == "toctree" for entry in self_toctree)
    return val


def get_pygments_style_colors(
    style: Style, *, fallbacks: Dict[str, str]
) -> Dict[str, str]:
    """Get background/foreground colors for given pygments style."""
    background = style.background_color  # type: ignore[attr-defined]
    text_colors = style.style_for_token(Text)  # type: ignore[attr-defined]
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


def _compute_hide_toc(
    context: Dict[str, Any],
    *,
    builder: StandaloneHTMLBuilder,
    docname: str,
) -> bool:
    # Should the table of contents be hidden?
    file_meta = context.get("meta", None) or {}
    if "hide-toc" in file_meta:
        return True
    elif "toc" not in context:
        return True
    elif not context["toc"]:
        return True

    return has_not_enough_items_to_show_toc(builder, docname)


@lru_cache(maxsize=None)
def _asset_hash(path: str) -> str:
    """Append a `?digest=` to an url based on the file content."""
    full_path = THEME_PATH / "static" / path
    digest = hashlib.sha1(full_path.read_bytes()).hexdigest()

    return f"_static/{path}?digest={digest}"


def _add_asset_hashes(static: List[str], add_digest_to: List[str]) -> None:
    if sphinx.version_info >= (7, 1):
        # https://github.com/sphinx-doc/sphinx/pull/11415 added the relevant
        # functionality to Sphinx, so we don't need to do anything.
        return

    for asset in add_digest_to:
        try:
            index = static.index("_static/" + asset)
        except ValueError:
            raise ConfigError(
                "Furo is trying to add a digest to an asset that is not in the "
                f"static files: {asset}. Please check conf.py for overrides of "
                "theme-provide assets such as `html_style`."
            )

        # Make this idempotent
        if "?digest=" in static[index].filename:  # type: ignore[attr-defined]
            continue
        static[index].filename = _asset_hash(asset)  # type: ignore[attr-defined]


def _fix_canonical_url(
    app: sphinx.application.Sphinx, pagename: str, context: Dict[str, Any]
) -> None:
    """Fix the canonical URL when using the dirhtml builder.

    Sphinx builds a canonical URL if ``html_baseurl`` config is set. However,
    it builds a URL ending with ".html" when using the dirhtml builder, which is
    incorrect. Detect this and generate the correct URL for each page.
    """
    if (
        not app.config.html_baseurl
        or not isinstance(app.builder, DirectoryHTMLBuilder)
        or not context["pageurl"]
        or not context["pageurl"].endswith(".html")
    ):
        return

    target = app.builder.get_target_uri(pagename)
    context["pageurl"] = app.config.html_baseurl + target


def _html_page_context(
    app: sphinx.application.Sphinx,
    pagename: str,
    templatename: str,
    context: Dict[str, Any],
    doctree: Any,
) -> None:
    if "css_files" in context:
        _add_asset_hashes(
            context["css_files"],
            ["styles/furo.css", "styles/furo-extensions.css"],
        )
    if "scripts" in context:
        _add_asset_hashes(
            context["scripts"],
            ["scripts/furo.js"],
        )

    _fix_canonical_url(app, pagename, context)

    # Basic constants
    context["furo_version"] = __version__

    # Values computed from page-level context.
    context["furo_navigation_tree"] = _compute_navigation_tree(context)
    context["furo_hide_toc"] = _compute_hide_toc(
        context, builder=cast(StandaloneHTMLBuilder, app.builder), docname=pagename
    )

    assert _KNOWN_STYLES_IN_USE["light"]
    assert _KNOWN_STYLES_IN_USE["dark"]
    # Inject information about styles
    context["furo_pygments"] = {
        "light": get_pygments_style_colors(
            _KNOWN_STYLES_IN_USE["light"],
            fallbacks=dict(
                foreground="black",
                background="white",
            ),
        ),
        "dark": get_pygments_style_colors(
            _KNOWN_STYLES_IN_USE["dark"],
            fallbacks=dict(
                foreground="white",
                background="black",
            ),
        ),
    }


def _builder_inited(app: sphinx.application.Sphinx) -> None:
    if "furo" in app.config.extensions:
        raise ConfigError(
            "Did you list 'furo' in the `extensions` in conf.py? "
            "If so, please remove it. Furo does not work with non-HTML builders "
            "and specifying it as an `html_theme` is sufficient."
        )

    looks_like_html_builder = isinstance(app.builder, StandaloneHTMLBuilder) or (
        app.builder.name in {"html", "dirhtml"}
    )
    if not looks_like_html_builder:
        raise ConfigError(
            "Furo is being used as an extension in a non-HTML build. "
            "This should not happen."
        )

    # Our JS file needs to be loaded as soon as possible.
    app.add_js_file("scripts/furo.js", priority=200)

    # 500 is the default priority for extensions, we want this after this.
    app.add_css_file("styles/furo-extensions.css", priority=600)

    builder = app.builder
    assert (
        builder.highlighter is not None  # type: ignore[attr-defined]
    ), "there should be a default style known to Sphinx"
    assert (
        builder.dark_highlighter is None  # type: ignore[attr-defined]
    ), "this shouldn't be a dark style known to Sphinx"
    update_known_styles_state(app)

    def _update_default(key: str, *, new_default: Any) -> None:
        try:
            conf_py_settings = app.config._raw_config
        except AttributeError:
            pass  # Sphinx's config has changed.
        else:
            if key not in conf_py_settings:
                app.config._raw_config.setdefault(key, new_default)

    # Change the default permalinks icon
    _update_default("html_permalinks_icon", new_default="#")


def update_known_styles_state(app: sphinx.application.Sphinx) -> None:
    """Update a global store of known styles of this application."""
    global _KNOWN_STYLES_IN_USE

    _KNOWN_STYLES_IN_USE = {
        "light": _get_light_style(app),
        "dark": _get_dark_style(app),
    }


def _get_light_style(app: sphinx.application.Sphinx) -> Style:
    # fmt: off
    # For https://github.com/psf/black/issues/3869
    return (  # type: ignore[no-any-return]
        app
            .builder
            .highlighter # type: ignore[attr-defined]
            .formatter_args["style"]
        )
    # fmt: on


def _get_dark_style(app: sphinx.application.Sphinx) -> Style:
    dark_style = app.config.pygments_dark_style
    return cast(Style, PygmentsBridge("html", dark_style).formatter_args["style"])


def _get_styles(formatter: "HtmlFormatter[str]", *, prefix: str) -> Iterator[str]:
    """Get styles out of a formatter, where everything has the correct prefix."""
    for line in formatter.get_linenos_style_defs():  # type: ignore[no-untyped-call]
        yield f"{prefix} {line}"
    yield from formatter.get_background_style_defs(prefix)  # type: ignore[no-untyped-call]
    yield from formatter.get_token_style_defs(prefix)  # type: ignore[no-untyped-call]


def get_pygments_stylesheet() -> str:
    """Generate the theme-specific pygments.css.

    There is no way to tell Sphinx how the theme handles dark mode; at this time.
    """
    light_formatter = PygmentsBridge.html_formatter(style=_KNOWN_STYLES_IN_USE["light"])
    dark_formatter = PygmentsBridge.html_formatter(style=_KNOWN_STYLES_IN_USE["dark"])

    lines: List[str] = []

    lines.extend(_get_styles(light_formatter, prefix=".highlight"))

    lines.append("@media not print {")

    dark_prefix = 'body[data-theme="dark"] .highlight'
    lines.extend(_get_styles(dark_formatter, prefix=dark_prefix))

    not_light_prefix = 'body:not([data-theme="light"]) .highlight'
    lines.append("@media (prefers-color-scheme: dark) {")
    lines.extend(_get_styles(dark_formatter, prefix=not_light_prefix))
    lines.append("}")

    lines.append("}")

    return "\n".join(lines)


# Yup, we overwrite the default pygments.css file, because it can't possibly respect
# the needs of this theme.
def _overwrite_pygments_css(
    app: sphinx.application.Sphinx,
    exception: Optional[Exception],
) -> None:
    if exception is not None:
        return

    assert app.builder
    with open(
        os.path.join(app.builder.outdir, "_static", "pygments.css"),
        "w",
        encoding="utf-8",
    ) as f:
        f.write(get_pygments_stylesheet())


def setup(app: sphinx.application.Sphinx) -> Dict[str, Any]:
    """Entry point for sphinx theming."""
    app.require_sphinx("6.0")

    app.add_config_value(
        "pygments_dark_style", default="native", rebuild="env", types=[str]
    )

    app.add_html_theme("furo", str(THEME_PATH))

    app.add_post_transform(WrapTableAndMathInAContainerTransform)

    app.connect("html-page-context", _html_page_context)
    app.connect("builder-inited", _builder_inited)
    app.connect("build-finished", _overwrite_pygments_css)

    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
        "version": __version__,
    }
