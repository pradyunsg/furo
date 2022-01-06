# Hiding Contents sidebar

Furo supports hiding the "Contents" sidebar (right), and does so automatically for any pages that don't have any inner headings.

To explicitly hide it on a specific page, `hide-toc` can be set in the [File-Wide metadata][sphinx-file-wide-metadata] for that page.

````{tab} reStructuredText
```rst
:hide-toc:

[page contents]
```
````

````{tab} Markdown (MyST)
```yaml
---
hide-toc: true
---

[page contents]
```
````

# "Edit page online" button

You can also optionally display a "Edit page" button. In your local conf if you include:

```
html_theme_options = {
    'web_base_url' : '<your base url>'
}
```

The Contents sidebar will include a "Edit page online" button that will link to the appropriate page based on the base url.

For Github, this base url is probably similar to `https://github.com/<github_user>/<github_repo>/edit/<branch>/docs`

This repository has the base url as: `https://github.com/pradyunsg/furo/edit/main/docs`.

If you would like the button to include your vcs host, you can add another option:

```
html_theme_options = {
    'web_base_url' : '<your base url>'
    'vcs_host': '<vcs host>'
}
```

For example, if `vcs_host` is set to 'Github', then the button text would say: "Edit page on Github".

[sphinx-file-wide-metadata]: https://www.sphinx-doc.org/en/master/usage/restructuredtext/field-lists.html#metadata
