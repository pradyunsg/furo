# Recommendations

This page lists a few opinionated recommendations for Sphinx plugins to use in your documentation along with Furo. All these plugins work well with Furo-based Sphinx documentation, but they are not inherently tied to Furo.

[MyST (Markedly Structured Text)][MyST]
: This project enables writing documentation with Markdown in Sphinx[^using-markdown]. This is achieved by making well-thought-out extensions to the CommonMark Specification, which make it as capable as reStructuredText. In case you're wondering if that works well... this documentation is written using MyST.

  Markdown is a significantly more popular markup format than reStructuredText. This means that it's likely that potential contributors/developers on the project are significantly more familiar with Markdown than reStructuredText. MyST gives you the best of both worlds -- simplicity and familiarity of Markdown with the extensibility power of reST.

[sphinx-opengraph]
: This project automagically adds Open Graph meta tags to your site's generated HTML. The Open Graph protocol is used by social media websites to determine how to present a page when a link is posted, and by search engines as a criterion toward ranking.

[sphinx-inline-tabs]
: This project provides a straightforward way to introduce tabbed content within your documentation. This is useful for instructions specific to something about the end user (like their OS, or preferred language, etc). This is a great way to organise complex bits of documentation without major trouble.

  Disclaimer: I am the creator and the primary maintainer of sphinx-inline-tabs.

[sphinx-autobuild]
: This project provides a live-reloading server, that rebuilds the documentation and refreshes any open pages automatically when changes are saved. This enables a much shorter feedback loop which can help boost productivity when writing documentation. Furo's development workflow is based on [uses this project](contributing/workflow.md#local-development-server).

  Disclaimer: I am the primary maintainer of sphinx-autobuild.

[sphinx-copybutton]
: This project adds a convenient copy button to code blocks. This is a subtle but effective user experience improvement when there are code snippets that a user might wish to copy from (examples, sample code etc).

In addition to the above, a shoutout to the [Executable Books] project which maintains many useful [Sphinx extensions][ebp-extensions] including some listed above.

[^using-markdown]: MyST addresses all the concerns that have been raised when arguing against [Using Markdown for Technical Documentation][dont-use-markdown], which really only leaves us with the good bits. :)

[MyST]: https://myst-parser.readthedocs.io/en/latest/
[sphinx-autobuild]: https://github.com/executablebooks/sphinx-autobuild#readme
[sphinx-copybutton]: https://github.com/executablebooks/sphinx-copybutton#readme
[sphinx-inline-tabs]: https://github.com/pradyunsg/sphinx-inline-tabs#readme
[sphinx-opengraph]: https://github.com/wpilibsuite/sphinxext-opengraph
[executable books]: https://executablebooks.org
[ebp-extensions]: https://github.com/executablebooks/?q=sphinx

[dont-use-markdown]: https://www.ericholscher.com/blog/2016/mar/15/dont-use-markdown-for-technical-docs/
