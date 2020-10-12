# Changing landing page

It is possible to have a custom landing page in Sphinx documentation. This is achieved by adding a custom template file for that page and setting [`html_additional_pages`][additional-pages] in `conf.py`.

```py
templates_path = ["_templates"]
html_additional_pages = {
    "index": "your-custom-landing-page.html"
}
```

```{note}
You'll need to write HTML for the page in `_templates/your-custom-landing-page.html`, if you use the above example as-is.
```

In case you're curious, this works because Sphinx allows overwriting existing files when generating the website and processes `html_additional_pages` _after_ processing the pages normally. These two behaviours combined mean that we can overwrite the page generated with the default layout by specifying the same document with a different template in `html_additional_pages`.

[additional-pages]: https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_additional_pages
