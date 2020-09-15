# Configuration file for the Sphinx documentation builder.
#
# Full list of options can be found in the Sphinx documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

#
# -- sys.path preparation ----------------------------------------------------
#

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent / "demo"))


#
# -- Project information -----------------------------------------------------
#

project = "furo"
copyright = "2020, Pradyun Gedam"
author = "Pradyun Gedam"

#
# -- General configuration ---------------------------------------------------
#

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.mathjax",
    "sphinx.ext.todo",
    "myst_parser",
    "sphinx_panels",
]
templates_path = ["_templates"]

#
# -- Options for TODOs -------------------------------------------------------
#
todo_include_todos = True

#
# -- Options for Markdown files ----------------------------------------------
#
myst_admonition_enable = True
myst_deflist_enable = True

#
# -- Options for HTML output -------------------------------------------------
#

html_logo = "_static/logo.png"
html_theme = "furo"
html_title = "furo"

html_static_path = ["_static"]
html_theme_options = {
    "sidebar_hide_name": True,
    "announcement": (
        "Furo is under active development, and this documentation is not written yet!"
    ),
}
