# Workflow

This page describes the tooling used during development of this project. It also serves as a reference for the various commands that you would use when working on this project.

## Overview

This project uses the [GitHub Flow] for collaboration and [nox] for automating development tasks. The codebase contains Python code, [Jinja2]-based HTML pages, [SASS] stylesheets and vanilla JS. The [SASS] and JS files are compiled into the final CSS and JS files used by the theme, with a [Gulp]-based build pipeline for assets. [sphinx-autobuild] is used to provide live-reloading pages when working on the theme. [pre-commit] is used for running the linters.

## Initial Setup

To work on this project, you need to have a git 2.17+, Python 3.6+ and NodeJS 12.

* Clone this project using git:

    ```
    git clone https://github.com/pradyunsg/furo.git
    cd furo
    ```

* Install the project's dependencies:

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

* Run this command, and wait from the browser window to open.
* <kbd>alt</kbd>+<kbd>tab</kbd> gets me back to my text editor.
* Make changes to some files and save those changes.
* <kbd>alt</kbd>+<kbd>tab</kbd> switches to the browser.
* After a small delay, the change is reflected in the browser.
* If I want to make more changes, <kbd>alt</kbd>+<kbd>tab</kbd> and I'm back to my text editor.
* Repeat the last 4 steps until happy.

\- @pradyunsg
:::

### Documentation Generation

```
nox -s docs
```

Generate the documentation for furo into the `build/docs` folder. This (mostly) does the same thing as `nox -s docs`, except it invokes `sphinx-build` instead of [sphinx-autobuild].

## Release process

```{note}
There are plans to automate this entire flow, with a `nox -s release` command.
```

* Checkout the current master, and ensure the working directory is clean
* Remove build/ and dist/ -- `rm -r build/ dist/` on *nix
* Bump the version in `src/furo/__init__.py`
* Run `flit build`
* Run `twine check dist/*`
* Commit changes and create a tag.
* Run `twine upload dist/*`
* Bump the version in `src/furo/__init__.py`
* Commit changes
* Push it all

[GitHub Flow]: https://guides.github.com/introduction/flow/
[nox]: https://nox.readthedocs.io/en/stable/
[BDFL]: https://en.wikipedia.org/wiki/Benevolent_dictator_for_life
[Jinja2]: https://jinja.palletsprojects.com
[SASS]: https://sass-lang.com
[Gulp]: https://gulpjs.com
[sphinx-autobuild]: https://github.com/executablebooks/sphinx-autobuild
[pre-commit]: https://pre-commit.com/
