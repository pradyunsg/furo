# Admonitions

Admonitions are a great way to include side content, without significantly interrupting the document flow. Sphinx provides several different types of admonitions and allows for the inclusion and nesting of arbitrary content.

## Basic Usage

````{furo-demo}
```{note} This is what the most basic admonitions look like.
```

```{note}
It is *possible* to have multiple paragraphs in the same admonition.

If you really want, you can even have lists, or code, or tables.
```

This is from Markdown.

+++

.. note:: This is what the most basic admonitions look like.


.. note::
   It is *possible* to have multiple paragraphs in the same admonition.

   If you really want, you can even have lists, or code, or tables.


This is from reStructuredText.
````

## Custom Titles

````{furo-demo}
```{admonition} Look ma! A custom title.
It looks different though.
```

```{admonition} Another Custom Title
:class: note

Maaa! I made it look the same by setting the class.
```

+++

.. admonition:: Look ma! A custom title.

   It looks different though.


.. admonition:: Another Custom Title
   :class: note

   Maaa! I made it look the same by setting the class.

````

## Supported types

### `admonition`

```{admonition} The one with the custom titles.
It's got a certain charm to it.
```

### `attention`

```{attention}
Climate change is real.
```

### `caution`

```{caution}
Cliff ahead: Don't drive off it.
```

### `danger`

```{danger}
Mad scientist at work!
```

### `error`

```{error}
Does not compute.
```

### `hint`

```{hint}
Insulators insulate, until they are subject to ______ voltage.
```

### `important`

```{important}
Tech is not neutral, nor is it apolitical.
```

### `note`

```{note}
This is a note.
```

### `seealso`

```{seealso}
Other relevant information.
```

### `tip`

```{tip}
25% if the service is good.
```

### `todo`

This needs the `sphinx.ext.todo` extension.

```{todo}
Figure out why this extension uses `admonition-todo` as the class, instead of using `todo` (like every other admonition style in Sphinx).
```

### `warning`

```{warning}
Reader discretion is strongly advised.
```

## Nesting admonitions

``````{furo-demo}
`````{note}
You can nest admonitions.

````{warning}
But you really should not.

```{danger}
It's distracting.
```

And can be confusing for the user to understand.
````

And, honestly, looks weird.
`````

+++

.. note::

   You can nest admonitions.

   .. warning::

      But you really should not.

      .. danger::

         It's distracting.

      And can be confusing for the user to understand.

   And, honestly, looks weird.

``````

## Custom Admonitions

It is possible to define custom admonitions for use with Furo. This is done by
[including custom CSS](../customisation/injecting.md) in the site.

Borrowing from the [equivalent example for mkdocs-material][mkdocs-custom],
the CSS would be something like:

```css
:root {
  --icon--pied-piper: url('data:image/svg+xml;charset=utf-8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512"><path d="M244 246c-3.2-2-6.3-2.9-10.1-2.9-6.6 0-12.6 3.2-19.3 3.7l1.7 4.9zm135.9 197.9c-19 0-64.1 9.5-79.9 19.8l6.9 45.1c35.7 6.1 70.1 3.6 106-9.8-4.8-10-23.5-55.1-33-55.1zM340.8 177c6.6 2.8 11.5 9.2 22.7 22.1 2-1.4 7.5-5.2 7.5-8.6 0-4.9-11.8-13.2-13.2-23 11.2-5.7 25.2-6 37.6-8.9 68.1-16.4 116.3-52.9 146.8-116.7C548.3 29.3 554 16.1 554.6 2l-2 2.6c-28.4 50-33 63.2-81.3 100-31.9 24.4-69.2 40.2-106.6 54.6l-6.3-.3v-21.8c-19.6 1.6-19.7-14.6-31.6-23-18.7 20.6-31.6 40.8-58.9 51.1-12.7 4.8-19.6 10-25.9 21.8 34.9-16.4 91.2-13.5 98.8-10zM555.5 0l-.6 1.1-.3.9.6-.6zm-59.2 382.1c-33.9-56.9-75.3-118.4-150-115.5l-.3-6c-1.1-13.5 32.8 3.2 35.1-31l-14.4 7.2c-19.8-45.7-8.6-54.3-65.5-54.3-14.7 0-26.7 1.7-41.4 4.6 2.9 18.6 2.2 36.7-10.9 50.3l19.5 5.5c-1.7 3.2-2.9 6.3-2.9 9.8 0 21 42.8 2.9 42.8 33.6 0 18.4-36.8 60.1-54.9 60.1-8 0-53.7-50-53.4-60.1l.3-4.6 52.3-11.5c13-2.6 12.3-22.7-2.9-22.7-3.7 0-43.1 9.2-49.4 10.6-2-5.2-7.5-14.1-13.8-14.1-3.2 0-6.3 3.2-9.5 4-9.2 2.6-31 2.9-21.5 20.1L15.9 298.5c-5.5 1.1-8.9 6.3-8.9 11.8 0 6 5.5 10.9 11.5 10.9 8 0 131.3-28.4 147.4-32.2 2.6 3.2 4.6 6.3 7.8 8.6 20.1 14.4 59.8 85.9 76.4 85.9 24.1 0 58-22.4 71.3-41.9 3.2-4.3 6.9-7.5 12.4-6.9.6 13.8-31.6 34.2-33 43.7-1.4 10.2-1 35.2-.3 41.1 26.7 8.1 52-3.6 77.9-2.9 4.3-21 10.6-41.9 9.8-63.5l-.3-9.5c-1.4-34.2-10.9-38.5-34.8-58.6-1.1-1.1-2.6-2.6-3.7-4 2.2-1.4 1.1-1 4.6-1.7 88.5 0 56.3 183.6 111.5 229.9 33.1-15 72.5-27.9 103.5-47.2-29-25.6-52.6-45.7-72.7-79.9zm-196.2 46.1v27.2l11.8-3.4-2.9-23.8zm-68.7-150.4l24.1 61.2 21-13.8-31.3-50.9zm84.4 154.9l2 12.4c9-1.5 58.4-6.6 58.4-14.1 0-1.4-.6-3.2-.9-4.6-26.8 0-36.9 3.8-59.5 6.3z"/></svg>');
}
.admonition.pied-piper {
  border-color: rgb(43, 155, 70);
}
.admonition.pied-piper > .admonition-title {
  background-color: rgba(43, 155, 70, 0.1);
  border-color: rgb(43, 155, 70);
}
.admonition.pied-piper > .admonition-title::before {
  background-color: rgb(43, 155, 70);
  -webkit-mask-image: var(--icon--pied-piper);
  mask-image: var(--icon--pied-piper);
}
```

With this, you can now use this by setting the `:class: pied-piper` on an
admonition:

````{furo-demo}

```{admonition} Pied Piper
:class: pied-piper

This is neat, right?
```

This is from Markdown.

+++

.. admonition:: Pied Piper
   :class: pied-piper

   This is neat, right?


This is from reStructuredText.

````

[mkdocs-custom]: https://squidfunk.github.io/mkdocs-material/reference/admonitions/#custom-admonitions
