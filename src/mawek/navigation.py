"""Generate the navigation tree from Sphinx's toctree function's output."""

import functools

from bs4 import BeautifulSoup


@functools.lru_cache
def get_navigation_tree(toctree_html):
    """Modify the given navigation tree, with mawek-specific elements.

    Adds a checkbox + corresponding label to <li>s that contain a <ul> tag, to enable
    the I-spent-too-much-time-making-this-CSS-only collapsing sidebar tree.

    """
    soup = BeautifulSoup(toctree_html, "html.parser")

    toctree_checkbox_count = 0
    for element in soup.find_all("li"):
        if not element.find("ul"):
            continue

        # This is an <li> with children.
        classes = element.get("class", [])
        element["class"] = classes + ["has-children"]

        # Add the checkbox that's used to store expanded/collapsed state.
        toctree_checkbox_count += 1
        checkbox_name = f"toctree-checkbox-{toctree_checkbox_count}"
        checkbox = soup.new_tag(
            "input",
            attrs={
                "type": "checkbox",
                "class": ["toctree-checkbox"],
                "id": checkbox_name,
                "name": checkbox_name,
            },
        )
        if "current" in classes:
            checkbox.attrs["checked"] = ""
        element.insert(1, checkbox)

        # Add the "label" for the checkbox which will get filled.
        label = soup.new_tag("label", attrs={"for": checkbox_name})
        element.insert(1, label)

    return str(soup)
