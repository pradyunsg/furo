# Adding a logo

Logos are a point of recognition and an important part of branding. Furo supports adding your project's logo at the top of the navigational (left) sidebar, like most other Sphinx themes.

## Same logo for light and dark mode

Furo supports the standard Sphinx mechanism to add your project's logo in the documentation, using the [`html_logo`][sphinx-html_logo] variable in `conf.py`.

```python
html_logo = "logo.png"
```

## Different logos for light and dark mode

Furo also supports setting different logos for light and dark mode. This can be necessary if the project's logo is transparent and does not maintain sufficient contrast with the background in both modes.

This is done by setting `light_logo` and `dark_logo` in [`html_theme_options`][sphinx-html_theme_options] in `conf.py`.

```python
html_static_path = ["_static"]
html_theme_options = {
    "light_logo": "logo-light-mode.png",
    "dark_logo": "logo-dark-mode.png",
}
```

```{important}
The filenames must be relative to the [`html_static_path`][sphinx-html_static_path] folder. In the above example, that'd be `_static/logo-light-mode.png` and `_static/logo-dark-mode.png`.

This is different from how `html_logo` works, which copies the given filename into the correct location automagically.
```

## Related Information

It is also possible to [hide the name of the project in the sidebar](customisation/index.md#sidebar_hide_name), which might be desirable if the logo contains the project name.

[sphinx-html_logo]: https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_logo
[sphinx-html_theme_options]: https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_theme_options
[sphinx-html_static_path]: https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_static_path
