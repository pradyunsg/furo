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

project = "mawek"
copyright = "2020, Pradyun Gedam"
author = "Pradyun Gedam"

#
# -- General configuration ---------------------------------------------------
#

extensions = ["sphinx.ext.autodoc"]
templates_path = ["_templates"]

#
# -- Options for HTML output -------------------------------------------------
#

html_theme = "mawek"

html_static_path = ["_static"]
html_title = "mawek"
