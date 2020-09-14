# Customisation

```{todo}
This entire page is still a work-in-progress.
```

furo can be customized in many ways.

- provides a lot of points for customising the generated documentation
- is possible to tweak:
  - the overall theme's look
  - the sidebar's contents
  - selectively hide UI elements/TOC on a certain pages

```{toctree}
:caption: Reference for various elements
:maxdepth: 1

colors
fonts
nav-sidebar
toc-sidebar
admonitions
```

## Theme options

furo utilizes [`html_theme_options`][sphinx-html-theme-options] key in `conf.py` for customization of the overall theme.

### `css_variables`

```{todo}
This needs rewriting, and more... "prominence".
```

furo's stylesheet makes extensive use of [CSS variables][css-variables]. It is possible to change look and feel of the documentation.

`css_variables` provides an easy way to override furo's default values for these variables.

```python
html_theme_options = {
    "css_variables": {"color-brand-primary": "red", "color-brand-content": "#CC3333",}
}
```

```{note}
Typos in the `css_variables` dictionary are silently ignored, and do not raise any errors or warnings. Double check that your spellings and values are correct and valid.
```

### `sidebar_hide_name`

Controls whether you see the project's name in the sidebar of the documentation. This is useful when you only want to show your documentation's logo in the sidebar.

```python
html_theme_options = {
    "sidebar_hide_name": True,
}
```

```{important}
The configuration options that are inherited from the built-in `basic` Sphinx theme are *not* supported in furo.
```

## Custom CSS files

If you want more control than what is provided by the above theme options, you can add custom stylesheets to your documentation.

ReadTheDocs has an excellent explanation on [how to add custom CSS files][sphinx-custom-css] to Sphinx-based documentation.

## Page specific tweaks

It is possible to tell furo to hide certain elements in a single page, using [File-Wide metadata][sphinx-file-wide-metadata].

### `hide-toc`

When set, furo will not include the "contents" sidebar on that page.

```{todo}
Add support for some kind of tabbed UI, to make it nicer to show markdown/reST examples.
```

Markdown:

```yaml
---
hide-toc: true
---

```

reST:

```rst
:hide-toc:
```

[css-variables]: https://developer.mozilla.org/en-US/docs/Web/CSS/Using_CSS_custom_properties
[sphinx-html-theme-options]: https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_theme_options
[sphinx-custom-css]: https://docs.readthedocs.io/en/stable/guides/adding-custom-css.html
[sphinx-file-wide-metadata]: https://www.sphinx-doc.org/en/master/usage/restructuredtext/field-lists.html#metadata
