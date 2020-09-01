"""Selectively modify the structure of the HTML generated from sources."""

from bs4 import BeautifulSoup


def wrap_tables(content):
    """Wrap <table> elements in <div class="table-wrapper">."""
    soup = BeautifulSoup(content, "html.parser")

    for table in soup.find_all("table"):
        table_wrapper = soup.new_tag("div", attrs={"class": "table-wrapper"})
        table.replace_with(table_wrapper)
        table_wrapper.append(table)

    return str(soup)
