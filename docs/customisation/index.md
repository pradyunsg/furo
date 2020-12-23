# Customisation

Furo supports customisation of the theme's overall look and feel (through theme options) as well as a few per-page tweaks.

This section serves to guide the user with customising Furo-based documentation. This page lists all the theme-specific customisations, as provided by this theme. Other pages in this section provide guidance for making specific customisations when using Sphinx with Furo.

```{toctree}
:hidden:

logo
colors
fonts
landing-page
sidebar
toc
```

## Theme options

[`html_theme_options`][sphinx-html_theme_options] in `conf.py` is used for customisations that affect the entire documentation. This is for stuff like fonts and colors.

```{note}
Note that only the configuration options listed here are supported (not the ones inherited from the built-in `basic` Sphinx theme).
```

(css-variables)=

### `light_css_variables`/`dark_css_variables`

Furo makes extensive use of [CSS variables][css-variables]. These can be overridden by the user and are used for stylizing nearly all elements of the documentation.

Setting `*_css_variables` is the recommended mechanism to override Furo's default values for these variables.

```python
html_theme_options = {
    "light_css_variables": {
        "color-brand-primary": "red",
        "color-brand-content": "#CC3333",
        "color-admonition-background": "orange",
    },
}
```

```{caution}
Typos in the `*_css_variables` dictionary are silently ignored, and do not raise any errors or warnings. Double check that your spellings and values are correct and valid.
```

### `sidebar_hide_name`

Controls whether you see the project's name in the sidebar of the documentation. This is useful when you only want to show your documentation's logo in the sidebar. The default is `False`.

```python
html_theme_options = {
    "sidebar_hide_name": True,
}
```

### `navigation_with_keys`

Controls whether the user can navigate the documentation using the keyboard’s left and right arrows. The default is `False`.

```python
html_theme_options = {
    "navigation_with_keys": True,
}
```

## Page specific tweaks

[File-Wide metadata][sphinx-file-wide-metadata] is used for per-page customisation, primarily for controlling which UI elements are presented.

### `hide-toc`

The “Contents” sidebar is automatically hidden for any pages that don’t have any inner headings. It is possible to hide it even when a page has inner headings, by setting `hide-toc` at the page level. See {doc}`./toc` for an example.

## Custom CSS files

If you want more control than what is provided by the above theme options, you can add custom stylesheets to your documentation.

ReadTheDocs has an excellent explanation on [how to add custom CSS files][sphinx-custom-css] to Sphinx-based documentation.

[css-variables]: https://developer.mozilla.org/en-US/docs/Web/CSS/Using_CSS_custom_properties
[sphinx-html_theme_options]: https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_theme_options
[sphinx-custom-css]: https://docs.readthedocs.io/en/stable/guides/adding-custom-css.html
[sphinx-file-wide-metadata]: https://www.sphinx-doc.org/en/master/usage/restructuredtext/field-lists.html#metadata
