# Changelog

## 2021.04.11.beta34

- Account for even more variants of sidebar-caption HTML.

## 2021.04.11.beta33

- Another styling update sidebar-caption related changes in Sphinx.

## 2021.04.11.beta32

- Add a basic domainindex page, without dedicated styling.
- Add recommendation for sphinx-opengraph.
- Account for newer Sphinx versions changing classes for captions.
- Account for the broken docutils release.
- Right align viewcode links (like `[source]`) allowing wrapping of API
  signatures gradefully.

## 2021.03.20.beta31

- Get `pygments_dark_style` working.
- Use the correct layout for domain index placeholder.

## 2021.03.20.beta30

- Fix a typo in the README.
- Add an escape hatch for specific table of contents.

## 2021.03.19.beta29

- Update Python-Requires to >=3.6.
- Account for nested admonitions.
- Center align items like other themes.
- Don't stylize the compound `kbd` tags.
- Fix a broken internal link in documentation.
- Fix a mistyped vertical-align style.
- Vertically align embedded-in-text images.
- Declare in HTML that the theme's pages support multiple color schemes.

## 2021.02.28.beta28

- Fix a bug in how stylesheets are handled.
- Clarify how to install directly from GitHub.
- Document how to install from git.

## 2021.02.28.beta27

- Center figures and legends with `margin: auto`.
- Improve compatibility with `json` builder, by not passing functions into the
  Jinja templates.
- Add a friendly comment to `domainindex.html`, about it not being implemented.
- Add styling for GUI labels.

## 2021.02.27.beta26

- Fix wrong height on wide screens, for pages with a tall sidebar but not-tall
  content.
- Add type annotations to the codebase! 🎉
- Fix an instance of missing brackets in documentation.

## 2021.02.21.beta25

- Document how to inject custom code in Sphinx documentation
- Document that `pygments_dark_style` is Furo-specific
- Make `sphinx-panels` respond to dark mode with Furo
- Stop `defer`ing Javascript, which was causing search to break in some cases.

## 2020.12.30.beta24

- Disable environment caching if `pygments_dark_style` is changed.
- Revert to earlier background color for inline literals, and allow configuring
  it via a CSS variables.

## 2020.12.28.beta23

- Fix code-block overflow issue, introduced by the fix for sphinx-copybutton compatibility.
- Tweak horizontal rules, to always be 1px tall.
- Tweak background color for inline literals, to match code blocks.

## 2020.12.28.beta22

- MAJOR: Move theme files into a "furo" folder.
  - This affects any users deriving from furo's templates.
- Add (custom) support for `pygments_dark_style`.
- Add support for `genindex` pages.
  - Note that `html_split_index` is not supported at this time.
- Add support for highlighting API elements, when accessed via "#hash" in URL.
- Add `language_data.js` to search page, fixing `Stemmer` related failures in Sphinx 3.4.
- Document how to add a site-wide announcement.
- Fix sphinx-copybutton placement on scrollable code blocks.
- Generate an error page, for documents using `layout.html` from Sphinx's `basic` theme.
- Translate placeholder in sidebar's search.
- Tweak how additional h1 headings are handled in ToC sidebar.
- Update dependency constraints, limiting compatibility to Sphinx 3.x versions.

## 2020.12.09.beta21

- Rebuild theme assets, for main release.

## 2020.12.09.beta20

- Clarify expectations around sidebar customisation.
- Declare plugin information to pacify Sphinx's "are you parallel" check.
- Disable sidebar-follows-you-as-you-scroll Javascript.
- Fix scrollbar styles affecting document body.
- Tweak colors for problematic content.
- Tweak how words wrap in sidebar title.
- Tweak spacing in API documentation.
- Tweak wrapping of text in API function/class signatures.

## 2020.11.27.beta19

- Add styling for rubrics.
- Add styling for scrollbars, to make them match the theme.
- Fix bottom-of-page JS conditional.
- Fix stability of resources hashes. (thanks [@dvarrazzo](https://github.com/dvarrazzo))
- Fix styling for multi-term definition lists items.
- Re-add our development documentation kitchen-sink.
- Tweak how ToC sidebar handles scrollbars.
- Tweak styling for basic definition lists.

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
