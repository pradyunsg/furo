# Text Formatting

```{furo-demo}
Content can have inline markup like *emphasis*, **strong emphasis**,
`inline literals`, {sub}`subscript`, {sup}`superscript` and more!
You can even reference {pep}`13`. Yes, this is Markdown.

Hyperlinks can take various forms, so here's a list of them:

- standalone hyperlink: <https://python.org/>
- hyperlink using references: [link][markdown-external-hyperlink]
- hyperlink with inline URL: [link](https://python.org/)
- hyperlink to a different page: [link](../quickstart)
- hyperlink to a specific API element: {class}`pathlib.Path`

You can even have abbreviations like {abbr}`HTML (Hyper Text Markup Language)`.

[markdown-external-hyperlink]: https://python.org/

+++

Content can have inline markup like *emphasis*, **strong emphasis**,
``inline literals``, :sub:`subscript`, :sup:`superscript` and more!
You can even reference :pep:`13`. Yes, this is reStructuredText.

Hyperlinks can take various forms, so here's a list of them:

- standalone hyperlink: https://python.org/
- hyperlink using references: link_ (this is borked due to a MyST bug)
- hyperlink with inline URL: `link <https://python.org/>`_
- hyperlink to a different page: :any:`link <../quickstart>`
- hyperlink to a specific API element: :class:`pathlib.Path`

You can even have abbreviations like :abbr:`HTML (Hyper Text Markup Language)`.

.. _link: https://python.org/
```
