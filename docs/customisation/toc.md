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

[sphinx-file-wide-metadata]: https://www.sphinx-doc.org/en/master/usage/restructuredtext/field-lists.html#metadata
