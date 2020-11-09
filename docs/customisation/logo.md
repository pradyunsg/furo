# Adding a logo

Logos are a point of recognition and an important part of branding. Furo support adding your project's logo at the top of the navigational (left) sidebar, like most other Sphinx themes.

## Same logo for light and dark mode

Furo supports the standard Sphinx mechanism to add your project's logo in the documentation.

This is done by setting standard [`html_logo`][sphinx-html_logo] variable in `conf.py`.

```python
html_logo = "logo.png"
```

## Different logos for light and dark mode

Furo also supports setting different logos for light and dark mode. This can be necessary if the project's logo is transparent and does not maintain sufficient contrast with the background in both modes.

This is done by setting `light_logo` and `dark_logo` in [`html_theme_options`][sphinx-html_theme_options] in `conf.py`.

```python
html_theme_options = {
    "light_logo": "logo-light-mode.png",
    "dark_logo": "logo-dark-mode.png",
}
```

The filenames must be relative to the [`html_static_path`][sphinx-html_static_path] folder.

## Related Information

It is also possible to [hide the name of the project in the sidebar](customisation/index.md#sidebar_hide_name), which might be desirable if the logo contains the project name.

[sphinx-html_logo]: https://www.sphinx-doc.org/en/main/usage/configuration.html#confval-html_logo
[sphinx-html_theme_options]: https://www.sphinx-doc.org/en/main/usage/configuration.html#confval-html_theme_options
[sphinx-html_static_path]: https://www.sphinx-doc.org/en/main/usage/configuration.html#confval-html_static_path
