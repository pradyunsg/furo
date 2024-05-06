# Changing buttons on page

```{versionadded} 2022.02.14
Support for "edit this page" link.
```

```{versionadded} 2024.05.06
Support for "view this page" link.
```

Furo can add buttons to each document that links visitors to the document's sources on the repository's source control system.

This feature is inherited from [sphinx-basic-ng](https://sphinx-basic-ng.readthedocs.io/en/latest/), specifically the [`view-this-page.html`](https://sphinx-basic-ng.readthedocs.io/en/latest/usage/components/view-this-page/) and [`edit-this-page`](https://sphinx-basic-ng.readthedocs.io/en/latest/usage/components/edit-this-page/) components.

## With popular VCS hosts

Provide the relevant VCS variables, by setting the following keys in [`html_theme_options`][sphinx-html_theme_options]:

```python
html_theme_options = {
    "source_repository": "https://github.com/pradyunsg/furo/",
    "source_branch": "main",
    "source_directory": "docs/",
}
```

This model supports github.com, gitlab.com and bitbucket.org as domain names for the `source_repository` key.

## With arbitrary URLs

```{versionadded} 2022.09.29
`source_edit_link`
```

```{versionadded} 2024.05.06
`source_view_link`
```

Use arbitrary URLs for the view/edit buttons, by setting the following keys in [`html_theme_options`][sphinx-html_theme_options]:

```python
html_theme_options = {
    "source_edit_link": "https://my.awesome.host.example.com/awesome/project/edit/{filename}",
    "source_view_link": "https://my.awesome.host.example.com/awesome/project/view/{filename}",
}
```

The `{filename}` component will be replaced with the full path to the file, as known from the base of the documentation directory.

```{important}
Furo does not enforce that the `source_edit_link` / `source_view_link` contain `{filename}` or any sort of correctness check on these URLs. Make sure to manually confirm that the link works.
```

## Linking to copied sources

If [`html_show_sourcelink`](https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_show_sourcelink) and [`html_copy_source`](https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_copy_source) are `True` (which are the defaults), and the documentation does not configure any of the above variables, the view button will link to the raw sources copied in by Sphinx.

## Read the Docs support

```{versionadded} 2022.02.14

```

```{note}
This feature is only available for projects hosted on GitHub.
```

Furo has built-in support for inferring details from Read the Docs' environment for GitHub projects and enabling these buttons.

For such projects, Furo will try to automatically infer the source repository, branch, and directory from the Read the Docs build environment unless the above configuration variable are set.

### Edit button on Read the Docs

The _edit_ button will link to GitHub's edit view for the document.

### View button on Read the Docs

The _view_ button will link to the raw sources copied in by Sphinx, if available, [as noted above](#linking-to-copied-sources). If raw sources are not copied, it will link to GitHub's plain view for the document.

If you do not want to link to copied sources, you can set the following in the `conf.py`:

```python
html_copy_source = False
html_show_sourcelink = False
```

### Disabling on Read the Docs

```{versionadded} 2022.06.04

```

```{versionchanged} 2024.05.06
`top_of_page_buttons` replaces the singular `top_of_page_button`.
```

If you wish to disable these default buttons, use {ref}`top_of_page_buttons` and set it to `[]`.

[sphinx-html_theme_options]: https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_theme_options
