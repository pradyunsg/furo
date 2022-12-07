# Text Formatting

Text formatting is an important aspect of written text. Sphinx provides support for several ways to apply specific formatting.

```{furo-demo}
Content can have inline markup like *emphasis*, **strong emphasis**,
`inline literals`, {sub}`subscript`, {sup}`superscript` and so much more.
Providing a reference to {pep}`8` is straightforward. You can also include
abbreviations like {abbr}`HTML (Hyper Text Markup Language)`.

> This is blockquoted text.

It is possible to have multiple paragraphs of text, which get separated
from each other visually. When stronger visual separation is desired, a
horizontal separator can be used (3 or more punctuation characters on a line).

---

This is written in Markdown.

+++

Content can have inline markup like *emphasis*, **strong emphasis**,
``inline literals``, :sub:`subscript`, :sup:`superscript` and so much more.
Providing a reference to :pep:`8` is straightforward. You can also include
abbreviations like :abbr:`HTML (Hyper Text Markup Language)`.

    This is blockquoted text.

It is possible to have multiple paragraphs of text, which get separated
from each other visually. When stronger visual separation is desired, a
horizontal separator can be used (4 or more punctuation characters on a line).

----

This is written in reStructuredText.
```
