# Changelog

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
