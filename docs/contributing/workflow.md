# Workflow

This page describes the tooling used during development of this project. It also serves as a reference for the various commands that you would use when working on this project.

## Overview

This project uses the [GitHub Flow] for collaboration. The codebase contains Python code, [Jinja2]-based HTML pages, [Sass] stylesheets and Javascript code.

- [nox] is used for automating development tasks.
- [Gulp]-based build pipeline is used to process the Sass and Javascript files.
- [sphinx-autobuild] is used to provide live-reloading pages when working on the theme.
- [pre-commit] is used for running the linters.

## Initial Setup

To work on this project, you need to have git 2.17+, Python 3.6+ and NodeJS 12.

- Clone this project using git:

  ```
  git clone https://github.com/pradyunsg/furo.git
  cd furo
  ```

- Install the project's dependencies:

  ```
  npm install
  pip install nox
  ```

You're all set for working on this project.

## Commands

### Code Linting

```
nox -s lint
```

Run the linters, as configured with [pre-commit].

### Local Development Server

```
nox -s docs-live
```

Serve this project's documentation locally, using [sphinx-autobuild]. This will open the generated documentation page in your browser.

The server also watches for changes made to the documentation (`docs/`) or theme (`src/`), which will trigger a rebuild. Once the build is completed, server will automagically reload any open pages using livereload.

:::{tip}
My workflow, when I'm working on this theme, is along the lines of:

- Run this command, and wait for the browser window to open.
- <kbd>alt</kbd>+<kbd>tab</kbd> gets me back to my text editor.
- Make changes to some files and save those changes.
- <kbd>alt</kbd>+<kbd>tab</kbd> switches to the browser.
- After a small delay, the change is reflected in the browser.
- If I want to make more changes, <kbd>alt</kbd>+<kbd>tab</kbd> and I'm back to my text editor.
- Repeat the previous 4 steps until happy.

\- @pradyunsg
:::

### Documentation Generation

```
nox -s docs
```

Generate the documentation for Furo into the `build/docs` folder. This (mostly) does the same thing as `nox -s docs-live`, except it invokes `sphinx-build` instead of [sphinx-autobuild].

## Release process

- Update the changelog
- Run `nox -s release`
- Once that command succeeds, you're done!

## Installing directly from GitHub

There are times when you might want to install the in-development version of Furo (mostly for testing that a fix actually does fix things).

Furo cannot be installed directly using pip with the Git repository directly. This is because the Git repository does not contained the compiled CSS/JS. The distributions on PyPI have the compiled assets (because they're platform agnostic and plain text).

```sh
# Clone the repository
git clone https://github.com/pradyunsg/furo.git
cd furo
# Build the static assets
npm install
./node_modules/.bin/gulp build
# Install with pip
pip install .
```

[github flow]: https://guides.github.com/introduction/flow/
[nox]: https://nox.readthedocs.io/en/stable/
[jinja2]: https://jinja.palletsprojects.com
[sass]: https://sass-lang.com
[gulp]: https://gulpjs.com
[sphinx-autobuild]: https://github.com/executablebooks/sphinx-autobuild
[pre-commit]: https://pre-commit.com/
