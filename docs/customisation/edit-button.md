# Adding an edit button

Furo can add a small edit button to each document.

This is automatically added, when the documentation is generated on Read the Docs using a GitHub repository as the source. It is possible to provide this, outside of Read the Docs, by setting the following keys in {any}`html_theme_options`:

```python
html_theme_options = {
  "source_repository": "https://github.com/pradyunsg/furo/",
  "source_branch": "main",
  "source_directory": "docs/",
}
```

## Disabling on Read the Docs

If you're building documentation on Read the Docs using a GitHub repository as the source, the edit button is enabled by default. If you wish to disable this, use {ref}`top_of_page_button`.
