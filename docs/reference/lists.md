# Lists

Lists are useful because they emphasize certain information in regular text. They can able be used to enumerate or provide an easier reference. Sphinx allows for various forms of lists, each of which can be used in a different manner.

## Bullet Lists

```{furo-demo}
- Bullet lists in Markdown are pretty straightforward.
- A bunch of bullet points.
  - Nested bullets should be indented by two or more spaces.
  - They can just "show up" inline with the rest of the list. Adding blank lines
    before and after is also permitted.
- It is also possible to have multiple paragraphs in a bullet.

  Make sure to have a blank line between the paragraphs, and to indent the
  paragraphs to the correct level.

+++

- Bullet lists in reStructuredText are fairly straightforward.
- A bunch of bullet points.

  - Nested bullets should be indented by **exactly** two spaces.
  - They also need a blank line before and after them, otherwise it doesn't
    work right.

- It is also possible to have multiple paragraphs in a bullet.

  Make sure to have a blank line between the paragraphs, and to indent the
  paragraphs to the correct level.

```

## Numbered Lists

```{furo-demo}
1. Numbered lists are not complicated.
2. They do exactly what you think they do.

+++

1. Numbered lists are not complicated.
2. They do exactly what you think they do.

```

## Definition Lists

```{furo-demo}
Definition Lists
:  An extremely useful tool for describing stuff.

Complicated Term
:  Definition

+++

Definition Lists
   An extremely useful tool for describing stuff.

Complicated Term
   Definition
```
