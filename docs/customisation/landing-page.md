# Adding a landing page

It is possible to have a custom landing page in Sphinx documentation. This requires  To do this, you need to:

```py
html_additional_pages = {
    "index": "home.html"
}
```

This works since Sphinx will copy this file *after* writing the rest.

```{todo}
Flesh this out, with a cute example?
```
