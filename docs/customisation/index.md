# Customisation

Furo supports customisation of the theme's overall look and feel (through theme options) as well as a few per-page tweaks.

This section serves to guide the user with customising Furo-based documentation. This page lists all the theme-specific customisations, as provided by this theme. Other pages in this section provide guidance for making specific customisations when using Sphinx with Furo.

```{toctree}
:hidden:

logo
announcement
top-of-page-buttons
colors
fonts
footer
landing-page
sidebar
sidebar-title
toc
injecting
```

## Theme options

[`html_theme_options`][sphinx-html_theme_options] in `conf.py` is used for customisations that affect the entire documentation. This is for stuff like fonts and colors. While this theme inherits some options from the built-in `basic` Sphinx theme, only the ones documented here are supported.

(css-variables)=

### `light_css_variables` / `dark_css_variables`

```{versionadded} 2020.08.14.beta5

```

```{versionchanged} 2020.11.01.beta14
Support for dark mode involved replacing `css_variables` with `light_css_variables` / `dark_css_variables`.
```

Furo makes extensive use of [CSS variables][css-variables]. These can be overridden by the user and are used for stylizing nearly all elements of the documentation. {doc}`colors` contains important details of how these variables are used.

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

(sidebar_hide_name)=

### `sidebar_hide_name`

```{versionadded} 2020.08.14.beta5

```

Controls whether you see the project's name in the sidebar of the documentation. This is useful when you only want to show your documentation's logo in the sidebar. The default is `False`.

```python
html_theme_options = {
    "sidebar_hide_name": True,
}
```

### `navigation_with_keys`

```{versionadded} 2020.11.01.beta14

```

Controls whether the user can navigate the documentation using the keyboard’s left and right arrows. The default is `False`.

```python
html_theme_options = {
    "navigation_with_keys": True,
}
```

(top_of_page_button)=

### `top_of_page_button`

```{versionadded} 2022.06.04

```

```{deprecated} 2024.05.06
This will be removed after 2024-11-01. Use `top_of_page_buttons` instead.
```

Controls which button is shown on the top of the page. The only supported values are `"edit"` (the default) and `None`.

```python
html_theme_options = {
    "top_of_page_button": "edit",
}
```

(top_of_page_buttons)=

### `top_of_page_buttons`

```{versionadded} 2024.05.06

```

Controls which buttons are shown on the top of the page. This is a list which can be empty or contain one-or-more of the following values:

- `"edit"`
- `"view"`

```python
html_theme_options = {
    "top_of_page_buttons": ["view", "edit"],
}
```

### `announcement`

```{versionadded} 2020.12.28.beta22

```

Add a site-wide announcement, to the top of every page when set. See {doc}`./announcement` for the details.

### `footer_icons`

```{versionadded} 2022.02.14

```

Changes the icons presented in the site footer. See {doc}`./footer` for the details.

## Page specific tweaks

[File-Wide metadata][sphinx-file-wide-metadata] is used for per-page customisation, primarily for controlling which UI elements are presented.

### `hide-toc`

```{versionadded} 2020.08.14.beta5

```

The "Contents" sidebar is automatically hidden for any pages that don’t have any inner headings. It is possible to hide it even when a page has inner headings, by setting `hide-toc` at the page level. See {doc}`./toc` for an example.

## Custom CSS files

If you want more control than what is provided by the above theme options, see {doc}`injecting`.

[css-variables]: https://developer.mozilla.org/en-US/docs/Web/CSS/Using_CSS_custom_properties
[sphinx-html_theme_options]: https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_theme_options
[sphinx-file-wide-metadata]: https://www.sphinx-doc.org/en/master/usage/restructuredtext/field-lists.html#metadata
