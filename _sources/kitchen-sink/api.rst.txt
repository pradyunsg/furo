..
   Copyright (c) 2021 Pradyun Gedam
   Licensed under Creative Commons Attribution-ShareAlike 4.0 International License
   SPDX-License-Identifier: CC-BY-SA-4.0

*****************
API documentation
*****************

Using Sphinx's :any:`sphinx.ext.autodoc` plugin, it is possible to auto-generate documentation of a Python module.

.. tip::
    Avoid having in-function-signature type annotations with autodoc,
    by setting the following options:

    .. code-block:: python

        # -- Options for autodoc ----------------------------------------------------
        # https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html#configuration

        # Automatically extract typehints when specified and place them in
        # descriptions of the relevant function/method.
        autodoc_typehints = "description"

        # Don't show class signature with the class' name.
        autodoc_class_signature = "separated"

.. automodule:: furo._demo_module
    :members:

C inline signature
------------------

.. c:type:: my_type

This works :c:type:`my_type`, but I would like to point
to a pointer of the type (:c:expr:`my_type *`).
