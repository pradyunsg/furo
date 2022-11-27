# Adding an edit button

Furo can add a small edit button to each document to allow visitors to easily propose changes to that document using the repository's source control system.

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

Use arbitrary URLs for the edit button, by setting the following key in [`html_theme_options`][sphinx-html_theme_options]:

```python
html_theme_options = {
    "source_edit_link": "https://my.awesome.host.example.com/awesome/project/edit/{filename}",
}
```

The `{filename}` component will be replaced with the full path to the file, as known from the base of the documentation directory.

```{important}
Furo does not enforce that the `source_edit_link` contains `{filename}` or any sort of correctness check on this URL. Make sure to manually confirm that the link works.
```

## Read the Docs support

If you're building documentation on Read the Docs using a github.com-hosted repository as the source, the edit button is enabled by default.

### Disabling on Read the Docs

If you wish to disable this, use {ref}`top_of_page_button` and set it to `None`.

[sphinx-html_theme_options]: https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_theme_options
