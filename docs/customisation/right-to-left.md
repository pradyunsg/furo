# Changing text and layout to right-to-left

Furo makes it fairly straightforward to change the text direction across the entire documentation set, by indicating the desired text direction to the browser and adapting the layout accordingly.

This is done by setting `is_rtl` in [`html_theme_options`][sphinx-html_theme_options] in `conf.py`.

```python
html_theme_options = {
    "is_rtl": True,
}
```
