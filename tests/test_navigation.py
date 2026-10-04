"""Tests for Furo's sidebar navigation rendering."""

from furo.navigation import _NavigationTree, get_navigation_tree


class _FakeBuilder:
    """Minimal HTML builder stub for relative links."""

    def __init__(self, pagename):
        self.pagename = pagename

    def get_relative_uri(self, from_, to):
        """Return the relative URI from the current page to a target docname."""
        assert from_ == self.pagename
        return {
            ("guide/install", "intro"): "../intro.html",
            ("guide/install", "guide"): "../guide.html",
            ("guide/install", "guide/install"): "",
            ("guide/install", "guide/usage"): "usage.html",
            ("intro", "intro"): "",
            ("intro", "guide"): "guide.html",
            ("intro", "guide/install"): "guide/install.html",
            ("intro", "guide/usage"): "guide/usage.html",
        }[(from_, to)]


_TOKEN_TO_DOCNAME = {
    "__doc_0__": "intro",
    "__doc_1__": "guide",
    "__doc_2__": "guide/install",
    "__doc_3__": "guide/usage",
}


_TOCTREE_TEMPLATE = """\
<ul>
<li class="toctree-l1"><a class="reference internal" href="__doc_0__">Intro &amp; Setup <!-- omit in toc --></a></li>
<li class="toctree-l1"><a class="reference internal" href="__doc_1__">Guide</a><ul>
<li class="toctree-l2"><a class="reference internal" href="__doc_2__">Install</a></li>
<li class="toctree-l2"><a class="reference internal" href="__doc_3__">Usage</a></li>
</ul></li>
</ul>"""


def _render_cached_navigation(pagename):
    """Render the cached navigation tree for a page."""
    tree = _NavigationTree(
        get_navigation_tree(_TOCTREE_TEMPLATE), token_to_docname=_TOKEN_TO_DOCNAME
    )
    return tree.render(builder=_FakeBuilder(pagename), pagename=pagename)


def test_navigation_tree_renders_current_leaf_like_sphinx_toctree():
    """The cached tree renders a nested current leaf like the old code path."""
    expected_toctree = """\
<ul class="current">
<li class="toctree-l1"><a class="reference internal" href="../intro.html">Intro &amp; Setup <!-- omit in toc --></a></li>
<li class="toctree-l1 current"><a class="reference internal" href="../guide.html">Guide</a><ul class="current">
<li class="toctree-l2 current"><a class="current reference internal" href="#">Install</a></li>
<li class="toctree-l2"><a class="reference internal" href="usage.html">Usage</a></li>
</ul></li>
</ul>"""

    assert _render_cached_navigation("guide/install") == get_navigation_tree(
        expected_toctree
    )


def test_navigation_tree_renders_current_toplevel_like_sphinx_toctree():
    """The cached tree renders a top-level current page like the old code path."""
    expected_toctree = """\
<ul class="current">
<li class="toctree-l1 current"><a class="current reference internal" href="#">Intro &amp; Setup <!-- omit in toc --></a></li>
<li class="toctree-l1"><a class="reference internal" href="guide.html">Guide</a><ul>
<li class="toctree-l2"><a class="reference internal" href="guide/install.html">Install</a></li>
<li class="toctree-l2"><a class="reference internal" href="guide/usage.html">Usage</a></li>
</ul></li>
</ul>"""

    assert _render_cached_navigation("intro") == get_navigation_tree(expected_toctree)
