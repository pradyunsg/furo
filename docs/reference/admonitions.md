# Admonitions

Admonitions are a great way to include side content, without significantly interrupting the document flow. Sphinx provides several different types of admonitions and allows for the inclusion and nesting of arbitrary content.

## Basic Usage

````{furo-demo}
```{note}
This is what the most basic admonitions look like in Markdown.
```

```{note}
It is *possible* to have multiple paragraphs in the same admonition.

If you really want, you can even have lists, or code, or tables.
```


+++

.. note:: This is what the most basic admonitions look like in reStructuredText.

.. note::
   It is *possible* to have multiple paragraphs in the same admonition.

   If you really want, you can even have lists, or code, or tables.


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

`admonition`

:  ```{admonition} The one with the custom titles.
   It's got a certain charm to it.
   ```

`attention`

:  ```{attention}
   Climate change is real.
   ```

`caution`

:  ```{caution}
   Cliff ahead: Don't drive off it.
   ```

`danger`

:  ```{danger}
   Mad scientist at work!
   ```

`error`

:  ```{error}
   Does not compute.
   ```

`hint`

:  ```{hint}
   Insulators insulate, until they are subject to ______ voltage.
   ```

`important`

:  ```{important}
   Tech is not neutral, nor is it apolitical.
   ```

`note`

:  ```{note}
   This is a note.
   ```

`seealso`

:  ```{seealso}
   Other relevant information.
   ```

`tip`

:  ```{tip}
   25% if the service is good.
   ```

`todo`

:  This needs the `sphinx.ext.todo` extension.
:  ```{todo}
   Figure out why this extension uses `admonition-todo` as the class, instead of using `todo` (like every other admonition style in Sphinx).
   ```

`warning`

:  ```{warning}
   Reader discretion is strongly advised.
   ```

## Custom Admonitions

```{todo}
Describe the CSS variables needed.
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
