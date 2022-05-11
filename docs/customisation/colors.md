# Changing colors

Furo allows customising colors to fit your brand's identity, by using CSS variables. These can be declared directly in [`html_theme_options`][sphinx-html_theme_options], in your `conf.py`.

## How light and dark mode work

Furo is in light mode by default, switching to the dark mode when requested by the user's browser (through `prefers-color-scheme: dark`).

As a consequence of this design, the dark mode inherits the variable definitions from the light mode, only overriding specific values to adapt the theme. While the mechanism for switching between light/dark mode is not configurable, the exact CSS variable definitions used in this process can be configured.

It is possible to use different content for light and dark mode, by setting
`only-dark` and `only-light` classes on the content. This is the
[recommended approach](light-dark-images) for handling images with backgrounds.

## Using your own colors

Furo allows defining [CSS variables that overrides its default values](css-variables). The exact variable names to use can be found in Furo's source code [here](https://github.com/pradyunsg/furo/tree/main/src/furo/assets/styles/variables).

This mechanism allows configuring nearly every facet of Furo's design, including spacing between various items and the colors of nearly every component.

````{admonition} Example
Changing Furo's blue accent (used for stylising links, sidebar's content etc) to a purple one:

```py
html_theme_options = {
    "light_css_variables": {
        "color-brand-primary": "#7C4DFF",
        "color-brand-content": "#7C4DFF",
    },
}
```
````

## Code block styling

Furo does not directly handle highlighting of the code blocks. This is done by Sphinx, and is configurable using [`pygments_style`][sphinx-pygments_style] and `pygments_dark_style` in `conf.py`.

```py
pygments_style = "sphinx"
pygments_dark_style = "monokai"
```

```{note}
`pygments_dark_style` is Furo-specific at this time.
```

[sphinx-html_theme_options]: https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_theme_options
[sphinx-pygments_style]: https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-pygments_style
