# Changing footer icons

Furo allows customising the icons that are presented in the page footer. These icons can be used to link to relevant resources for your project and documentation.

```{admonition} Unstable, seeking feedback
:class: caution

This feature is treated as "unstable" under Furo's {doc}`../stability`.

It currently needs input from documentation authors, about how useful and usable this is and how "ergonomic" it is.
```

## Default icons

Furo includes two default icons, when the documentation is built on Read the Docs:

- A link to the Read the Docs project page, for the documentation.
- A link to the GitHub repository, if configured as a GitHub project on RTD.

If the documentation is not built on Read the Docs, there are no icons included by default.

## Configuration

To add custom footer icons, you need to provide the `footer_icons` configuration value to Furo. If this configuration value is non-empty, the default footer icons are disabled.

The value for this configuration value is a list of dictionaries. Each dictionary needs to have the following structure:

- `name`: Describes what the destination location is. This is primarily for screen readers.
- `url`: Where clicking on the icon will take users.
- `html`: The exact raw HTML that is included as the "icon".
- `class`: This is included as-is in the class attribute of the `a` tag.

### Using embedded SVGs

This is what Furo does to include a GitHub icon in the footer of the site you're currently reading:

```python
html_theme_options = {
    "footer_icons": [
        {
            "name": "GitHub",
            "url": "https://github.com/pradyunsg/furo",
            "html": """
                <svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 16 16">
                    <path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"></path>
                </svg>
            """,
            "class": "",
        },
    ],
}
```

Since `html` is expected to be static HTML, you can not use relative paths to images included in the Sphinx documentation set, at least not without resorting to ugly hacks.[^1] Instead, it is recommended to either embed the image directly (eg: in an `svg` tag), or to link to images "outside" of the documentation.

It is generally preferable to use SVG images, that respect `currentColor`. A decently large set of common SVG-based icons can be found on: <https://react-icons.github.io/react-icons/>[^2].

### Using icon packs

You can use icon packs that provide icons, with the footer. Usually, icons pack have a non-negligible impact on first page load times and need more data needing to be downloaded. That said, you also get more convenient access to a well designed set of icons. :)

#### Font Awesome

```{note}
With the release of Font Awesome 6, Fonticons Inc has revamped the documentation to consistently upsell their [Kits](https://fontawesome.com/v6/docs/web/setup/use-kit). These kits can help reduce load times on pages but have limited number of page views, so we'll use Font Awesome via a CDN in this example.
```

If you wish to use Font Awesome icons in the footer, it's a two step process.

- Using `html_css_files`, add the CSS file(s) for Font Awesome.

  ```py
  html_css_files = [
      "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/fontawesome.min.css",
      "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/solid.min.css",
      "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/brands.min.css",
  ]
  ```

- Use `class` to use the relevant Font Awesome icons in `footer_icons`. You can search the [free Font Awesome icons](https://fontawesome.com/v6/search?s=solid%2Cbrands), and clicking on a specific icon shows the class you need to use. The configuration would look as follows:

  ```py
  html_theme_options = {
      "footer_icons": [
          {
              "name": "GitHub",
              "url": "https://github.com/pradyunsg/furo",
              "html": "",
              "class": "fa-brands fa-solid fa-github fa-2x",
          },
      ],
  }
  ```

  Note that the `fa-2x` is necessary to get a reasonable sized icon.

## Different icons for light mode vs dark mode

You can specify `only-light` or `only-dark` as the value for `class` in the dictionary. This mechanism exists primarily to help you use different `img` tags to present the same icon in a different colour.

[^1]: Yes, I'm aware that it can be argued that embedding raw HTML in a `conf.py` file is... ugly. :)
[^2]: You need to use your browser's developer tools to get the SVG directly from the page: inspect element + copy svg element (ctrl+c) + paste.
