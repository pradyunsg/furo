"""Development automation
"""

import datetime
import glob
import os

import nox

PACKAGE_NAME = "furo"
nox.options.sessions = ["lint", "test"]


#
# Helpers
#
def _determine_versions(current_version, date):
    """Returns (version_in_release, version_after_release)"""
    dev_num = int(current_version.rsplit(".dev", 1)[-1])
    today_version = date.strftime("%Y.%m.%d")

    if current_version.startswith(today_version):
        # There was a release earlier today. Let's tack on another version
        # number segment onto this to make it unique.
        return (
            today_version + f".{dev_num}",
            today_version + f".dev{dev_num+1}",
        )
    return (
        today_version,
        today_version + ".dev1",
    )


# fmt: off
assert (
    _determine_versions("2021.08.17.dev44", date=datetime.date(2021, 8, 17))
    == ("2021.08.17.44", "2021.08.17.dev45")
), "same day 1"
assert (
    _determine_versions("2021.08.17.dev1", date=datetime.date(2021, 8, 17))
    == ("2021.08.17.1", "2021.08.17.dev2")
), "same day 2"
assert (
    _determine_versions("2021.08.17.dev44", date=datetime.date(2021, 8, 18))
    == ("2021.08.18", "2021.08.18.dev1")
), "different day"
# fmt: on


def get_release_versions(version_file):
    marker = "__version__ = "

    with open(version_file) as f:
        for line in f:
            if line.startswith(marker):
                current_version = line[len(marker) + 1 : -2]
                break
        else:
            raise RuntimeError("Could not find current version.")

    return _determine_versions(current_version, date=datetime.date.today())


#
# Development Sessions
#
@nox.session(reuse_venv=True)
def docs(session):
    session.install("-r", "docs/requirements.txt")
    session.install(".")

    # Generate documentation into `build/docs`
    session.run("sphinx-build", "-b", "dirhtml", "-v", "docs/", "build/docs")


@nox.session(name="docs-live", reuse_venv=True)
def docs_live(session):
    session.install("-r", "docs/requirements.txt")
    session.install("-e", ".", "sphinx-theme-builder[cli]")

    # Generate documentation into `build/docs`
    session.run("stb", "serve", "docs/", *session.posargs)


@nox.session(reuse_venv=True)
def lint(session):
    session.notify("lint-pre-commit")
    session.notify("lint-mypy")


@nox.session(reuse_venv=True, name="lint-pre-commit")
def lint_pre_commit(session):
    session.install("pre-commit")

    args = list(session.posargs)
    args.append("--all-files")
    if "CI" in os.environ:
        args.append("--show-diff-on-failure")

    session.run("pre-commit", "run", *args)


@nox.session(reuse_venv=True, name="lint-mypy")
def lint_mypy(session):
    session.install(
        "-e", ".", "mypy", "types-docutils", "types-Pygments", "types-beautifulsoup4"
    )
    session.run("mypy", "src")


@nox.session
def test(session):
    session.install("-e", ".", "-r", "tests/requirements.txt")

    args = session.posargs or [
        "-n=auto",
        "--cov=src/",
        "--cov-report=term-missing",
        "--verbose",
    ]
    session.run("pytest", *args)


@nox.session
def release(session):
    version_file = f"src/{PACKAGE_NAME}/__init__.py"
    allowed_upstreams = [
        f"git@github.com:pradyunsg/{PACKAGE_NAME.replace('_', '-')}.git"
    ]

    release_version, next_version = get_release_versions(version_file)

    session.install(
        "keyring",
        "release-helper",
        "sphinx-theme-builder[cli]",
        "twine",
    )

    # Sanity Checks
    session.run("release-helper", "version-check-validity", release_version)
    session.run("release-helper", "version-check-validity", next_version)
    session.run("release-helper", "directory-check-empty", "dist")

    session.run("release-helper", "git-check-branch", "main")
    session.run("release-helper", "git-check-clean")
    session.run("release-helper", "git-check-tag", release_version, "--does-not-exist")
    session.run("release-helper", "git-check-remote", "origin", *allowed_upstreams)

    # Prepare release commit
    session.run("release-helper", "version-bump", version_file, release_version)
    session.run("git", "add", version_file, external=True)

    session.run(
        "git", "commit", "-m", f"Prepare release: {release_version}", external=True
    )

    # Build the package
    session.run("stb", "package")
    session.run("twine", "check", *glob.glob("dist/*"))

    # Tag the commit
    session.run(
        # fmt: off
        "git", "tag", release_version, "-m", f"Release {release_version}", "-s",
        external=True,
        # fmt: on
    )

    # Prepare back-to-development commit
    session.run("release-helper", "version-bump", version_file, next_version)
    session.run("git", "add", version_file, external=True)
    session.run("git", "commit", "-m", "Back to development", external=True)

    # Push the commits and tag.
    session.run("git", "push", "origin", "main", release_version, external=True)

    # Upload the distributions.
    session.run("twine", "upload", *glob.glob("dist/*"))
