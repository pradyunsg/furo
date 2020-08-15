"""Generate the navigation tree from Sphinx's toctree function's output."""

import functools

from bs4 import BeautifulSoup


@functools.lru_cache
def get_navigation_tree(toctree_html):
    soup = BeautifulSoup(toctree_html, "html.parser")

    # TODO: modify the TOCTree for getting useful stuff out of it.
    return str(soup)
