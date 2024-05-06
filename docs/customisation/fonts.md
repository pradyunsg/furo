# Changing fonts

```{versionadded} 2020.08.14.beta5

```

```{versionchanged} 2024.04.27
Add `font-stack--headings`.
```

Furo makes it fairly straightforward to change the fonts across the entire page.

This is done by changing the values of the relevant CSS variables: `font-stack` (for regular text), `font-stack--monospace` (for code blocks and inline code) and `font-stack--headings` (for headings). This can be done using Furo's [mechanism for setting CSS variables](css-variables) -- specifically by setting them as the fonts for the light mode (which is inherited by the dark mode).

```py
html_theme_options = {
    "light_css_variables": {
        "font-stack": "Arial, sans-serif",
        "font-stack--monospace": "Courier, monospace",
        "font-stack--headings": "Georgia, serif",
    },
}
```

```{note}
It is strongly recommended to not change the fonts unless there is a strong reason (such as brand identity).

Furo's default fonts are carefully selected to look good across all major platforms without requiring additional web font downloads, enabling faster page loads and higher quality text presentation.
```
