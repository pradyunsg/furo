"""A clean customisable Sphinx documentation theme."""

__version__ = "2021.09.22"

import hashlib
import logging
import os
import textwrap
from functools import lru_cache
from pathlib import Path
from typing import Any, Dict, List, Optional, cast

import sphinx.application
from bs4 import BeautifulSoup
from pygments.formatters import HtmlFormatter
from pygments.style import Style
from pygments.token import Text
from sphinx.builders.html import StandaloneHTMLBuilder
from sphinx.highlighting import PygmentsBridge

from .navigation import get_navigation_tree

THEME_PATH = (Path(__file__).parent / "theme" / "furo").resolve()

logger = logging.getLogger(__name__)

# GLOBAL STATE
_KNOWN_STYLES_IN_USE: Dict[str, Optional[Style]] = {
    "light": None,
    "dark": None,
}


@lru_cache(maxsize=None)
def has_not_enough_items_to_show_toc(toc: str) -> bool:
    """Check if the toc has one or fewer items."""
    assert toc

    soup = BeautifulSoup(toc, "html.parser")
    return len(soup.find_all("li")) <= 1


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
    style: Style, *, fallbacks: Dict[str, str]
) -> Dict[str, str]:
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

    return has_not_enough_items_to_show_toc(context["toc"])


@lru_cache(maxsize=None)
def _asset_hash(path: str) -> str:
    """Append a `?digest=` to an url based on the file content."""
    full_path = THEME_PATH / "static" / path
    digest = hashlib.sha1(full_path.read_bytes()).hexdigest()

    return f"_static/{path}?digest={digest}"


def _add_asset_hashes(static: List[str], add_digest_to: List[str]) -> None:
    for asset in add_digest_to:
        index = static.index("_static/" + asset)
        static[index].filename = _asset_hash(asset)  # type: ignore


def _html_page_context(
    app: sphinx.application.Sphinx,
    pagename: str,
    templatename: str,
    context: Dict[str, Any],
    doctree: Any,
) -> None:
    if app.config.html_theme != "furo":
        return

    if "css_files" in context:
        _add_asset_hashes(
            context["css_files"],
            ["styles/furo.css", "styles/furo-extensions.css"],
        )
    if "scripts" in context:
        _add_asset_hashes(
            context["scripts"],
            ["scripts/main.js"],
        )

    # Basic constants
    context["furo_version"] = __version__

    # Values computed from page-level context.
    context["furo_navigation_tree"] = _compute_navigation_tree(context)
    context["furo_hide_toc"] = _compute_hide_toc(context)

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

    # Patch the content
    if "body" in context:
        context["body"] = wrap_elements_that_can_get_too_wide(context["body"])


def _builder_inited(app: sphinx.application.Sphinx) -> None:
    if app.config.html_theme != "furo":
        return

    # Our `main.js` file needs to be loaded as soon as possible.
    app.add_js_file("scripts/main.js", priority=200)

    # 500 is the default priority for extensions, we want this after this.
    app.add_css_file("styles/furo-extensions.css", priority=600)

    builder = cast(StandaloneHTMLBuilder, app.builder)
    assert builder, "what?"
    assert (
        builder.highlighter is not None
    ), "there should be a default style known to Sphinx"
    assert (
        builder.dark_highlighter is None
    ), "this shouldn't be a dark style known to Sphinx"
    update_known_styles_state(app)


def update_known_styles_state(app: sphinx.application.Sphinx) -> None:
    """Update a global store of known styles of this application."""
    global _KNOWN_STYLES_IN_USE

    _KNOWN_STYLES_IN_USE = {
        "light": _get_light_style(app),
        "dark": _get_dark_style(app),
    }


def _get_light_style(app: sphinx.application.Sphinx) -> Style:
    return app.builder.highlighter.formatter_args["style"]


def _get_dark_style(app: sphinx.application.Sphinx) -> Style:
    # number_of_hours_spent_figuring_this_out = 7
    #
    # Hello human in the future! This next block of code needs a bit of a story, and
    # if you're going to touch it, remember to update the number above (or remove this
    # comment entirely).
    #
    # Hopefully, you know that Sphinx allows extensions and themes to add configuration
    # values via `app.add_config_value`. This usually lets users set those values from
    # `conf.py` while allowing the extension to read from it and utilise that information.
    # As any reasonable person who's written a Sphinx extension before, you would
    # expect the following to work:
    #
    #     dark_style = app.config.pygments_dark_style
    #
    # Turns out, no. How dare you expect things to just work!? That stuff just returns
    # the default value provided when calling `app.add_config_value`. Yes, even if you
    # set it in `conf.py`. Why? Good question. :)
    #
    # The logic in Sphinx literally looks it up in the same mapping as what was
    # manipulated by `add_config_value`, and there's no other spot where that value
    # gets manipulated. I spent a bunch of time debugging how that class works, and...
    # yea, I can't figure it out. There's multiple mappings floating around and bunch
    # of manipulation being done for all kinds of things.
    #
    # The only place on the config object where I was able to find the user-provided
    # value from `conf.py` is a private variable `self._raw_config`. Those values are
    # supposed to get added to self.__dict__[...], and generally be accessible through
    # the object's custom `__getattr__`.
    #
    # Anyway, after giving up on figuring out how to file a PR to fix this upstream, I
    # started looking for hacky ways to get this without reaching into private
    # variables. That quest led to a very simple conclusion: no, you can't do that.
    #
    # So, here we are: with the only option being to reach into the guts of the beast,
    # and pull out the specific thing that's needed. This is obviously fragile though,
    # so this is written with the assumption that any changes to Sphinx's config
    # object's internals would correspond to the originally expected behaviour working.
    # This is so that when any of Sphinx's internals change, this logic would basically
    # fall back to the original behaviour and also print a warning, so that hopefully
    # someone will report this. Maybe it'll all be fixed, and I can remove this whole
    # hack and this giant comment.

    # HACK: begins here
    dark_style = None
    try:
        if (
            hasattr(app.config, "_raw_config")
            and isinstance(app.config._raw_config, dict)
            and "pygments_dark_style" in app.config._raw_config
        ):
            dark_style = app.config._raw_config["pygments_dark_style"]
    except (AttributeError, KeyError) as e:
        logger.warn(
            (
                "Furo could not determine the value of `pygments_dark_style`. "
                "Falling back to using the value provided by Sphinx.\n"
                "Caused by %s"
            ),
            e,
        )

    if dark_style is None:
        dark_style = app.config.pygments_dark_style

    return PygmentsBridge("html", dark_style).formatter_args["style"]


def get_pygments_stylesheet() -> str:
    """Generate the theme-specific pygments.css.

    There is no way to tell Sphinx how the theme handles dark mode; at this time.
    """
    light_formatter = HtmlFormatter(style=_KNOWN_STYLES_IN_USE["light"])
    dark_formatter = HtmlFormatter(style=_KNOWN_STYLES_IN_USE["dark"])

    light = light_formatter.get_style_defs(".highlight")
    dark_one = dark_formatter.get_style_defs('body[data-theme="dark"] .highlight')
    dark_two = dark_formatter.get_style_defs(
        'body:not([data-theme="light"]) .highlight'
    )

    return textwrap.dedent(
        f"""
            {light}
            {dark_one}
            @media (prefers-color-scheme: dark) {{
                {dark_two}
            }}
        """
    )


# Yup, we overwrite the default pygments.css file, because it can't possibly respect
# the needs of this theme.
def _overwrite_pygments_css(
    app: sphinx.application.Sphinx,
    exception: Optional[Exception],
) -> None:
    if exception is not None:
        return

    assert app.builder
    with open(os.path.join(app.builder.outdir, "_static", "pygments.css"), "w") as f:
        f.write(get_pygments_stylesheet())


def setup(app: sphinx.application.Sphinx) -> Dict[str, Any]:
    """Entry point for sphinx theming."""
    app.require_sphinx("3.0")

    app.add_config_value(
        "pygments_dark_style", default="native", rebuild="env", types=[str]
    )

    app.add_html_theme("furo", str(THEME_PATH))

    app.connect("html-page-context", _html_page_context)
    app.connect("builder-inited", _builder_inited)
    app.connect("build-finished", _overwrite_pygments_css)

    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
        "version": __version__,
    }
