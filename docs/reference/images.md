# Images

Images can be a great supplement to technical documentation text. Sphinx provides control for their alignment in the content, as well as the ability to add captions.

## Basic Usage

```{furo-demo}
![](https://picsum.photos/id/237/200/200)

This is from Markdown.

+++

.. image:: https://picsum.photos/id/237/200/200

This is from reStructuredText.
```

## Alignment

````{furo-demo}
```{image} https://picsum.photos/id/237/200/200
:align: center
```

This is from Markdown.

+++

.. image:: https://picsum.photos/id/237/200/200
   :align: center


This is from reStructuredText.
````

## Captions

````{furo-demo}

```{figure} https://picsum.photos/id/237/200/200
This is a captioned image, which needs the "figure" directive.
```

This is from Markdown.

+++

.. figure:: https://picsum.photos/id/237/200/200

    This is a captioned image, which needs the "figure" directive.

This is from reStructuredText.
````

(light-dark-images)=

## Different images for dark/light mode

Furo supports [light mode and dark mode](../customisation/colors) colours
out-of-the-box. However, certain images do not work well against certain
backgrounds (eg: if the image has a white background).

You can use the `only-light` and `only-dark` classes, to show different images
based on the currently active colour scheme.

````{furo-demo}

```{image} https://picsum.photos/id/237/200/200
:align: center
:class: only-light
```

```{image} https://picsum.photos/id/237/200/200
:align: center
:class: only-dark
```

```{figure} https://picsum.photos/id/237/200/200
:align: center
:figclass: only-light
```

```{figure} https://picsum.photos/id/237/200/200
:align: center
:figclass: only-dark
```

This is from Markdown.

+++

.. image:: https://picsum.photos/id/237/200/200
   :align: center
   :class: only-light


.. image:: https://picsum.photos/id/237/200/200
   :align: center
   :class: only-dark


.. figure:: https://picsum.photos/id/237/200/200
   :align: center
   :figclass: only-light


.. figure:: https://picsum.photos/id/237/200/200
   :align: center
   :figclass: only-dark


This is from reStructuredText.

````
