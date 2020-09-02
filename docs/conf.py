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

extensions = ["sphinx.ext.autodoc", "sphinx.ext.mathjax", "myst_parser"]
templates_path = ["_templates"]

#
# -- Options for HTML output -------------------------------------------------
#

html_theme = "furo"
html_title = "Furo"

html_static_path = ["_static"]
