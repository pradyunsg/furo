# Adding an announcement banner

Furo makes it fairly straightforward to add a site-wide announcement (AKA top banner). The announcement is added to the top of all pages on the website.

This is done by setting `announcement` key in [`html_theme_options`][sphinx-html_theme_options] in your `conf.py` file. The value of this key is HTML, which is included as-is into the page.

```python
html_theme_options = {
    "announcement": "<em>Important</em> announcement!",
}
```

The background and foreground of the announcement element are customisable, via the mechanisms described in {doc}`colors`.

[sphinx-html_theme_options]: https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_theme_options
