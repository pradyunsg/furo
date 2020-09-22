# Internals

Furo's internals contain an interesting mix of stupid-things-that-work and all kinds of bodges. Most of this project was built slowly over the span of a few weeks, as a part of an attempt to take a break from working on Python packaging stuff.

## Repository Layout

```{todo}
Flesh this section out.
```

## Theme build process

Furo's build process uses Gulp. Running `gulp build` in the repository root will compile the theme's CSS and JS assets (`src/furo/assets/`) into the correct final files (inside `src/furo/theme/static`).

When building the distributions for upload, `gulp build` is run once and the `src/furo/assets/` directory is excluded for the final distribution. Thus, _both_ the source distribution and wheel distribution do not contain the original source code for Furo and only contain the compiled SCSS and JS files.

```{note}
It is not ideal that the version-controlled source tree is not installable using pip directly. There is a need for a `gulp build` command to be run between the clone and installation.

Things are set up this way due to the lack of a "build" step support in Flit. There is [an open issue for enhancement with a proposal awaiting feedback](https://github.com/takluyver/flit/issues/119#issuecomment-687779285).
```

## How stuff works

### Sidebar Navigation Tree

```{todo}
Flesh this section out, hopefully without burning brain cells like I did when designing this thing's collapse stuff.
```

### Contents sidebar

```{todo}
Flesh this section out.
```

### CSS variables for customisation

```{todo}
Flesh this section out.
```

### `furo-demo` directive

This directive was written to make it easier to write the examples used in the [Reference](../reference/index) section. The way it works is pretty straightforward really:

- It only works in MyST documents, since it performs an in-place substitution.
- It takes the contents of the block, splits it at "+++" into Markdown and reStructuredText snippets.
- For both of these, it renders a tab that has a code block containing the snippet followed by the actual code itself.
  - This is carefully crafted to ensure that things are evaluated correctly.

This approach has significant limitations however, since the A/B comparision format means that it is not directly usable to showcase functionality that is different between the two.

For that, we keep one of the snippets empty, which thanks to a conditional, results in the tab for that language (MyST or reST) not being rendered.
