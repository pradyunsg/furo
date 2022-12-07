# Injecting code

Sphinx makes it fairly straightforward to add custom JS/CSS/HTML code to your pages. Furo supports the mechanisms provided by Sphinx for this.

```{admonition} Unstable
:class: caution
This customisation considered "unstable" under Furo's {doc}`../stability`.

Customisations done directly with CSS/JS/HTML are unbounded. Furo is not designed to accommodate for custom CSS/JS/HTML in any meaningful way, and no effort is made to stay compatible with such customisations.
```

## CSS or JS

Read the Docs has an excellent explanation on [how to add custom CSS or JS files][sphinx-custom-css] to Sphinx-based documentation. No point repeating information in two places. 😄

[sphinx-custom-css]: https://docs.readthedocs.io/en/stable/guides/adding-custom-css.html

## HTML

This is entirely powered by Sphinx's templating mechanism, which is built upon {pypi}`Jinja2`.

The primary way to do this is to override the content of the Furo's default templates with your own templates, using [`templates_path`][sphinx-templates_path]. For more information on how to do so, [Sphinx's templating documentation][templating].

```{note}

The expectation is that users who override Furo's templates would also carefully consider how their documentation looks across various platforms (i.e. not take a "looks OK on my machine" approach) and would also be willing to extend Furo's CSS to make their HTML changes work well.
```

[sphinx-templates_path]: https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-templates_path
[templating]: https://www.sphinx-doc.org/en/master/development/theming.html#templating
