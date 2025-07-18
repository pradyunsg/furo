"""Sphinx Extensions to simplify writing Furo's Reference documentation.

This provides a single `furo-demo` directive, which:

- Only works when used in a MyST document.
- Requires sphinx-inline-tabs' tab directive.
- Requires contents to be of the following format:

    {lines-of-markdown}

    +++

    {lines-of-reStructuredText}

"""

from textwrap import indent
from typing import Any, Tuple

from docutils import nodes
from docutils.statemachine import StringList
from sphinx.application import Sphinx
from sphinx.directives import SphinxDirective  # type: ignore[attr-defined]


def _split_by_language(block_text: str) -> Tuple[str, str]:
    try:
        a, b = block_text.split("+++\n")
    except ValueError:
        if block_text.endswith("+++"):
            return block_text[:-3], ""
        raise RuntimeError("Expected separator line containing only '+++'.")
    else:
        return a, b


def _md_demo(block: str) -> StringList:
    lines = []
    if not block.strip("\n"):
        return StringList()

    lines.append("````````{tab} Markdown (MyST)")
    lines.append("```````md")
    lines.extend(block.splitlines())
    lines.append("```````")
    lines.extend(block.splitlines())
    lines.append("````````")

    return StringList(lines)


def _rst_demo(block: str) -> StringList:
    lines = []
    if not block.strip():
        return StringList()

    lines.append("````````{tab} reStructuredText")
    lines.append("```````{eval-rst}")
    lines.append(".. code-block:: rest")
    lines.append("")
    lines.extend(indent(block, "    ").splitlines())
    lines.append("")
    lines.extend(block.splitlines())
    lines.append("```````")
    lines.append("````````")

    return StringList(lines)


def _translate_into_tab_demo(block_text: str) -> StringList:
    md, rst = _split_by_language(block_text)

    string_list = StringList()

    string_list.extend(_rst_demo(rst))
    string_list.extend(_md_demo(md))

    return string_list


class _FuroDemoDirective(SphinxDirective):
    has_content = True

    def run(self) -> Any:
        self.assert_has_content()

        container = nodes.container()
        transated_content = _translate_into_tab_demo(self.block_text)
        self.state.nested_parse(transated_content, 0, container)
        return [container]


def setup(app: Sphinx) -> None:
    """For setting up the directive."""
    app.add_directive("furo-demo", _FuroDemoDirective)
