# Changing fonts

Furo makes it fairly straightforward to change the fonts across the entire page.

This is done by changing the values of the relevant CSS variables: `font-stack` (for regular text) and `font-stack--monospace` (for code blocks and inline code). This can be done using Furo's [mechanism for setting CSS variables](css-variables) -- specifically by setting them as the fonts for the light mode (which is inherited by the dark mode).

```py
html_theme_options = {
    "light_css_variables": {
        "font-stack": "Arial, sans-serif",
        "font-stack--monospace": "Courier, monospace",
    },
}
```

```{note}
It is strongly recommended to not change the fonts unless there is a strong reason (such as brand identity) since Furo's default fonts are carefully selected to look good across all major platforms.
```
