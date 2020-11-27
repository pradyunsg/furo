# Changelog

## 2020.11.19.beta18

- Fix search page. It had become non-operational, due to changes to JS
  in the previous release.

## 2020.11.15.beta17

- Add properly documented mechanisms for customising the sidebar.
- Add dedicated styling for ethical ads.
- Tweak how JS scripts are loaded.

## 2020.11.14.beta16

- Add a separate file for CSS that affects other Sphinx extensions.
- Add content to all the existing pages in documentation.
- Clarify that Furo is biased toward smaller documentation sets.
- Clarify that logo files need to be in `html_static_path`
- Improve various explanations in documentation.
- Tweak borders inside tables.
- Tweak bottom spacing on right sidebar.
- Tweak CSS and JS blocks in `base.html` template.
- Tweak how captions for toctrees look.
- Tweak spacing on sidebar ad on ReadTheDocs.

## 2020.11.10.beta15

- Add a recommendations page, for plugins
- Add support for different logos in light and dark mode
- Change location of TOC drawer icon on mobile
- Drop support for `html_sidebars` based customisation.
- Improve how the RTD ads work
- Improve TOC sidebar auto-scroll functional
- Significantly improve footer capabilities

## 2020.11.01.beta14

- Add classifiers to the theme.
- Add friendly messages for users of `html_sidebars`.
- Add link to homepage, in mobile header.
- Add support for ethical ads in the sidebar.
- Change `css_variables` to `light_css_variables`.
- Change font stack to match to GitHub.
- Change the color used for `<hr>` tags.
- Change unsplash URLs to use cute+animal as cues
- Document `navigation_with_keys`.
- Drop logic that jumps toc-scroll to bottom-of-page.
- Improve customisation documentation.
- Remove text underline from headerlink.
- Strip tags in title.

## 2020.10.15.beta13

- Add a direct dependency on Sphinx.
- Add styling for "highlighted text" in dark mode.
- Add support for sphinx-inline-tabs.
- Change the default development branch name to `main`.
- Drop customisations for sphinx-panel's tabs.
- Rework the entire handling of background and foreground colours.
- Tweak API documentation, when presented in dark mode.
- Tweak Bootstrap 4 `.container` styling (comes from sphinx-panel).
- Tweak borders on tables.
- Tweak dark mode colors.
- Tweak light mode colors.

## 2020.10.13.beta12

- Fix image link in README, to show up correctly on PyPI.

## 2020.10.13.beta11

- Tweak colors for dark mode.
- Tweak presentation of `<kbd>`, to look better in dark mode.

## 2020.10.13.beta10

- Add dark mode support, based on `prefers-color-scheme`! 🎉
- Add more information in the documentation (reference and customisation).
- Add sourcemaps in the generated distribution.
- Add support for glossary lists.
- Drop the custom ReadTheDocs-specific CSS.
- Fix bad transparency handling for sidebar hover on Safari.
- Fix shrinking of sidebar brand image on Safari.
- Tweak spacing in admonitions.

## 2020.10.05.beta9

- Add per-build hashes to asset URLs, to simplify cache invalidation.
- Tweak spacing in API documentation.

## 2020.09.28.beta8

- Require Sphinx 3.
- Add styling for API documentation.
- Add styling for abbreviations.
- Add `clear` CSS property for left/right aligned content.
- Add styling to tweak the look of tabs.
- Drop the complexities introduced for custom homepages.
- Tweak color of problematic content.
- Tweak font-size handling for code-blocks.
- Tweak font-size handling for admonitions.
- Tweak spacing around code-blocks.
- Tweak how pages look with announcement and shorter-than-viewport content.
- Tweak styling for lists.
- Fix overlays to correctly show on top of content.
- Restructure sidebar scrolling, to correctly fill viewport.
- Change JS from the basic theme to use blocking network requests.
- Change inline table of contents to look like an error, nudging toward to not using it.

## 2020.09.15.beta7

- Automate version management
- Use correct width for elements on small screens (100% instead of 100vw)

## 2020.09.15.beta6

- Tweak header on small screens.
- Tweak spacing for small screens.
- Place "sidebar" directive's contents inline, on small screens.

## 2020.08.14.beta5

```{important}
This release was not correctly versioned and is not installed preferentially over beta4.
```

- Add CSS variables for header foreground and background.
- Add styling for captions.
- Add styling for correctly handling permalinks.
- Correctly stylize _only_ definition lists with the rules intended for them.
- Fix next/prev links flowing into one-another by limiting width to 50%.
- Fix positioning of collapsed contents sidebar icon.
- Fix shrinking arrows in next/prev links.
- Include `basic` theme's JS files unconditionally. This should help with compatibility with various Sphinx extensions and ReadTheDocs.
- Make `math` elements scrollable, when wider than the page.
- Tweak images to be responsive.
- Tweak spacing of paragraphs.
- Tweak location of ReadTheDocs' injected version helper.

## 2020.9.8.beta4

- More fixes for Python 3.7 support.

## 2020.9.8.beta3

- Add support for `sphinx.ext.todo`.
- Add support for hiding name in sidebar.
- Add reference to deployed documentation in README.
- Tweak font size for admonitions.
- Tweak spacing for contents sidebar.
- Tweak styling of inline code.
- Fix support for Python < 3.8.

## 2020.9.8.beta2

- Add support for logos in the sidebar.
- Fix path used for search page.
- Tweak height for short pages on mobile (100vh resulted in a scroll).
- Tweak definition lists.
- Tweak line height in contents, to accommodate for code literals.
- Use `em` as the unit for layout sizes.
- Start writing theme's documentation.
- Deploy documentation on <https://pradyunsg.me/furo/>.

## 2020.9.2.beta1

Initial release.
