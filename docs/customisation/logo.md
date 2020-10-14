# Adding a logo

Logos are a point of recognition and an important part of branding. Furo supports the standard Sphinx mechanism to add your project's logo in the documentation. This is done by setting [`html_logo`][sphinx-html_logo] in `conf.py`:

```python
html_logo = "logo.png"
```

It is also possible to [hide the name of the project in the sidebar](customisation/index.md#sidebar_hide_name), which might be desirable if the logo contains the project name.

[sphinx-html_logo]: https://www.sphinx-doc.org/en/main/usage/configuration.html#confval-html_logo
