---
hide-toc: true
---

# Changelog

## 2020.09.14.beta5

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
