# API documentation

API documentation serves as an important reference in technical documentation. Sphinx provides many approaches to writing API documentation, from writing them manually as well as automatically generating it from docstrings in your code.

This example uses {any}`sphinx.ext.autodoc` for generating the API documentation skeleton. {any}`sphinx.ext.intersphinx` provides links for classes in type annotations.

````{furo-demo}
```{eval-rst}
.. autoclass:: urllib3.util.Retry
    :members:
    :noindex:

.. autoclass:: urllib3.util.Timeout
    :members:
    :noindex:
```

This is a small example from Markdown.

+++

.. autoclass:: urllib3.util.Retry
    :members:
    :noindex:

.. autoclass:: urllib3.util.Timeout
    :members:
    :noindex:

This is a small example from reStructuredText.

````
