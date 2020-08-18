"""Table of Contents-related Sphinx-context logic."""

from bs4 import BeautifulSoup

from functools import lru_cache


@lru_cache
def should_hide_toc(toc):
    """Determine whether toc has content beyond the initial heading."""
    if not toc:
        return True

    soup = BeautifulSoup(toc, "html.parser")
    if len(soup.find_all("li")) == 1:
        return True

    return False
