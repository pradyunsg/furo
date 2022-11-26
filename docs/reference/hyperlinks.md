# Hyperlinks

Hyperlinks are extremely useful for connecting related topics without having to depart from a clear linear exposition. Sphinx supports various formats for creating hyperlinks, with {any}`sphinx.ext.intersphinx` being a great tool for cross-documentation hyperlinks.

```{furo-demo}
Hyperlinks can take various forms, so here's a list of them:

- standalone hyperlink: <https://python.org/>
- hyperlink using references: [link][markdown-external-hyperlink]
- hyperlink with inline URL: [link](https://python.org/)
- hyperlink to a different page: [link](../quickstart)
- hyperlink to a specific API element: {class}`pathlib.Path`

[markdown-external-hyperlink]: https://python.org/

+++

Hyperlinks can take various forms, so here's a list of them:

- standalone hyperlink: https://python.org/
- hyperlink using references: `link <link>`__
- hyperlink with inline URL: `link <https://python.org/>`_
- hyperlink to a different page: :doc:`link <../quickstart>`
- hyperlink to a specific API element: :class:`pathlib.Path`

.. _link: https://python.org/
```
