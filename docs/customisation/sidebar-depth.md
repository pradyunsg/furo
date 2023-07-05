# Changing sidebar depth

By default, Furo includes your full site in the left sidebar's table of contents. This is intentional to have a good user experience: 

- users can easily navigate your whole site with fewer clicks, and
- they can easily see where they are in the site hierarchy.

However, for large projects, including the full site in the sidebar can result in two issues:

1. slow Sphinx build performance, and
2. large HTML page sizes, which slows down your site's initial load.

For example, large sidebars can be a problem when using [Sphinx's autosummary](https://www.sphinx-doc.org/en/master/usage/extensions/autosummary.html) with a large API.

You can limit the depth of the left sidebar by setting `navigation_depth` in `html_theme_options` in `conf.py` to a number like `2` or `3`. It defaults to `-1`.

```python
html_theme_options = {
    "navigation_depth": 4,
}
```

However, setting `navigation_depth` lower can result in a worse user experience navigating your site. Only set `navigation_depth` if you are having issues with Sphinx build times and/or the HTML page size. Experiment to find a number that balances those problems with keeping a good navigation experience.

Before changing `navigation_depth`, consider if you can reorganize your site to reduce the number of HTML pages. For example, with `autosummary`, consider changing its templates so that each function does not get a dedicated HTML page.

## Tip: consider dynamically setting `navigation_depth`

You can dynamically set the `navigation_depth` via an environment variable. That allows you to use a deeper `navigation_depth` like `-1` or `4` for your production builds, while using a lower number like `1` or `2` in development builds (e.g. CI) to speed up Sphinx.

For example:

```python
import os

html_theme_options = {
   "navigation_depth": os.getenv("NAVIGATION_DEPTH", -1)
}
```
