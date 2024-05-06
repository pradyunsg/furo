# Adding source code buttons

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

## Read the Docs support

```{versionchanged} 2024.05.06
This feature has been tentatively removed (but the removal has not been released), as a better approach is investigated. See [this discussion](https://github.com/pradyunsg/furo/discussions/785) for more details.
```

If you're building documentation on Read the Docs using a github.com-hosted repository as the source, the edit button is enabled by default.

### Disabling on Read the Docs

If you wish to disable this, use {ref}`top_of_page_button` and set it to `None`.

[sphinx-html_theme_options]: https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_theme_options
