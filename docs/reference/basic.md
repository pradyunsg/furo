# Basic Markup

## Inline Formatting

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
- hyperlink using references: link_
- hyperlink with inline URL: `link <https://python.org/>`_
- hyperlink to a different page: :any:`link <../quickstart>`
- hyperlink to a specific API element: :class:`pathlib.Path`

You can even have abbreviations like :abbr:`HTML (Hyper Text Markup Language)`.

.. _link: https://python.org/
```

## Lists

```{furo-demo}
- Lists in Markdown are pretty straightforward.
- A bunch of bullet points.
  - Nested bullets should be indented by two or more spaces.
  - They can just "show up" inline with the rest of the list.


1. Numbered lists are not complicated.
2. They do exactly what you think they do.

Definition Lists
:  An extremely useful tool for describing stuff.

Term
:  Definition
+++

- Lists in reStructuredText are fairly straightforward.
- A bunch of bullet points.

  - Nested bullets should be indented by **exactly** two spaces.
  - They also need a blank line before them, otherwise it doesn't work right.

1. Numbered lists are not complicated.
2. They do exactly what you think they do.

Definition Lists
   An extremely useful tool for describing stuff.

Term
   Definition
```

## Code

````{furo-demo}
```python
print("Hello from Markdown")
```

+++

.. code-block:: python

    print("Hello from reStructuredText")
````

## Images

```{furo-demo}
![](https://source.unsplash.com/200x200/daily?ferret)

This is from Markdown.

+++

.. image:: https://source.unsplash.com/200x200/daily?ferret

This is from reStructuredText.
```
