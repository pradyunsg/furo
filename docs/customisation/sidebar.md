# Changing sidebar elements

Furo supports customising the elements that show up in the navigational sidebar (left). This is to provide documentation authors who are willing to work with HTML/CSS to change and tweak how the sidebar looks.

```{warning}
Furo is not designed to accommodate for all potential custom sidebar designs. It is also possible to get suboptimal results (or even break the layout!) when overriding the default sidebar.
```

```{admonition} Info
:class: tip

The general expectation is that users who override the sidebar would also carefully consider how their documentation looks across various platforms (i.e. not take a "looks OK on my machine" approach) and would be willing to override Furo's styles to make it work with their sidebar design.

Some things to consider when doing this are:

- different OSs/browsers handle scrollbars and their widths differently,
  with different effects on the layouting
- end users can customise the look of their default scrollbars at an OS level(like overlay, hidden, visible-and-takes-space and maybe more?)
- different viewport heights will differ across devices
```

## Default design

The following code snippet lists the fragments (HTML files from Furo's theme folder) that are used for the default sidebar design.

```{literalinclude} ../../src/furo/theme/furo/theme.conf
---
language: ini
start-after: "# sidebar-start"
end-before: "# sidebar-end"
---
```

```{hint}
The scrollable region in the sidebar is determined by `sidebar/scroll-start.html` and `sidebar/scroll-end.html`. Any elements that fall between them can be scrolled.
```

## Making changes

There are two main ways to customise Furo's sidebar:

- override the content of the default templates with your own templates, using [`templates_path`][sphinx-templates_path].
- change the entire sidebar structure, using [`html_sidebars`][sphinx-html_sidebars].

### Using `templates_path`

This is useful when you want to change a specific element of the sidebar. A good example for when you might want to use this: adding a tagline after your project's name/logo.

This is done by setting [`templates_path`][sphinx-templates_path] in the `conf.py` and correctly adding files within the configured paths.

```python
templates_path = ["_templates"]
```

For the above example -- adding a tagline after the name/logo -- you'd want to add an `_templates/sidebar/brand.html` file, that overrides the appropriate content. For more information on how to do so, [Sphinx's templating documentation][templating].

### Using `html_sidebars`

This is useful when you want to make drastic or major changes to the design of Furo's sidebar.

As an example, to make the _entire_ sidebar scrollable, it is possible to set `sidebar/scroll-start.html` as the first fragment and `sidebar/scroll-end.html` as the last fragment.

```py
html_sidebars = [
    "sidebar/scroll-start.html",
    "sidebar/brand.html",
    "sidebar/search.html",
    "sidebar/navigation.html",
    "sidebar/ethical-ads.html",
    "sidebar/scroll-end.html",
]
```

```{warning}
`sidebar/scroll-start.html` and `sidebar/scroll-end.html` must be included in the sidebar. Ensure that the "non-scrollable" elements (i.e. that don't occur between these two) do not go beyond the height of the viewport.
```

```{tip}
If you're hosting your documentation on ReadTheDocs, please make sure that `sidebar/ethical-ads.html` is included in the sidebar. This helps keep ReadTheDocs sustainable.
```

[sphinx-templates_path]: https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-templates_path
[sphinx-html_sidebars]: https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_sidebars
[templating]: https://www.sphinx-doc.org/en/master/development/theming.html#templating
