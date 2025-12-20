"""Configuration file for the Sphinx documentation builder.

Full list of options can be found in the Sphinx documentation:
https://www.sphinx-doc.org/en/master/usage/configuration.html
"""

import os
import sys
from typing import Any, Dict

# add the demo python code to the path, so that it can be used to demonstrate
# source links
sys.path.append(os.path.abspath("./kitchen-sink/demo_py"))

# -- Project information -----------------------------------------------------
#

project = "furo"
copyright = "2020, Pradyun Gedam"
author = "Pradyun Gedam"

# -- General configuration ---------------------------------------------------
#

extensions = [
    # Sphinx's own extensions
    "sphinx.ext.autodoc",
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    # Our custom extension, only meant for Furo's own documentation.
    "furo.sphinxext",
    # External stuff
    "myst_parser",
    "sphinx_copybutton",
    "sphinx_design",
    "sphinx_inline_tabs",
]

# -- Options for Autodoc --------------------------------------------------------------

autodoc_member_order = "bysource"
autodoc_preserve_defaults = True

# Keep the type hints outside the function signature, moving them to the
# descriptions of the relevant function/methods.
autodoc_typehints = "description"

# -- Options for extlinks ----------------------------------------------------
#

extlinks = {
    "pypi": ("https://pypi.org/project/%s/", "%s"),
}

# -- Options for intersphinx -------------------------------------------------
#

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master", None),
}

# -- Options for TODOs -------------------------------------------------------
#

todo_include_todos = True

# -- Options for Markdown files ----------------------------------------------
#

myst_enable_extensions = [
    "colon_fence",
    "deflist",
]
myst_heading_anchors = 3

# -- Options for HTML output -------------------------------------------------
#

html_theme = "furo"
html_title = "Furo"
language = "en"

html_static_path = ["_static"]
html_css_files = ["pied-piper-admonition.css"]

html_theme_options: Dict[str, Any] = {
    "footer_icons": [
        {
            "name": "GitHub",
            "url": "https://github.com/pradyunsg/furo",
            "html": """
                <svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 16 16">
                    <path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"></path>
                </svg>
            """,
            "class": "",
        },
    ],
    "source_repository": "https://github.com/pradyunsg/furo/",
    "source_branch": "main",
    "source_directory": "docs/",
}

if "READTHEDOCS" in os.environ:
    html_theme_options["announcement"] = (
        "This documentation is hosted on Read the Docs only for testing. Please use "
        "<a href='https://pradyunsg.me/furo/'>the main documentation</a> instead."
    )

# -- Options for theme development -------------------------------------------
# Make sure these are all set to the default values.

html_js_files = []
html_context: Dict[str, Any] = {}
# html_show_sphinx = False
# html_show_copyright = False
# html_last_updated_fmt = ""

RTD_TESTING = False
if RTD_TESTING or "FURO_RTD_TESTING" in os.environ:
    del html_theme_options["footer_icons"]

    html_js_files += [
        # NOTE: I'm not including this file here yet. Are we mocking any HTTP
        # response somehow in the tests? In that case, we need to return this
        # JSON when hitting `/_/addons/`
        # https://furo.readthedocs.io/_/addons/?client-version=0.12.0&api-version=1&project-slug=furo&version-slug=latest
        # "readthedocs-addons-mocked-response.js",
        # NOTE: pinning to 0.12.0 for now, but we can use `main` if we want to
        "https://raw.githubusercontent.com/readthedocs/addons/0.12.0/dist/readthedocs-addons.js",
    ]
    html_context["READTHEDOCS"] = True

    # All of these won't be injected anymore.
    # They are not going to be used by Read the Docs Sphinx's theme either,
    # we should probably talk if they are required for furo.
    html_context["current_version"] = os.environ.get("READTHEDOCS_VERSION")
    html_context["slug"] = os.environ.get("READTHEDDOCS_PROJECT")

    # These cannot be replaced with environment variables. My understanding is
    # that these are used here to build the "Edit on GitHub" buttons. We don't
    # have a good way to replace this feature yet. There are some Git
    # environment variables that could be used to here to parse and get the
    # final URL. Example:
    # https://docs.readthedocs.io/en/stable/reference/environment-variables.html#envvar-READTHEDOCS_GIT_CLONE_URL
    # For now, Read the Docs is not including "View/Edit on GitHub" links
    # because of this reason. See
    # https://github.com/readthedocs/readthedocs.org/issues/10742 for a more
    # complete description of the issue and potential solutions
    #
    # html_context["conf_py_path"] = "/docs/"
    # html_context["display_github"] = True
    # html_context["github_user"] = "pradyunsg"
    # html_context["github_repo"] = "furo"
    # html_context["github_version"] = "main"

FONT_AWESOME_TESTING = False
if FONT_AWESOME_TESTING:
    html_css_files += [
        "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/fontawesome.min.css",
        "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/solid.min.css",
        "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/brands.min.css",
    ]

    html_theme_options["footer_icons"] = [
        {
            "name": "GitHub",
            "url": "https://github.com/pradyunsg/furo",
            "html": "",
            "class": "fa-brands fa-solid fa-github fa-2x",
        },
    ]
