"""Development automation
"""
import os
import re
import subprocess
import tempfile
from glob import glob
from pathlib import Path
from time import time

import nox

PACKAGE_NAME = "mawek"
nox.options.sessions = ["lint", "test"]


#
# Helpers
#
def _install_this_project_with_flit(session, *, extras=None, editable=False):
    session.install("flit")
    args = []
    if extras:
        args.append("--extras")
        args.append(",".join(extras))
    if editable:
        args.append("--pth-file" if os.name == "nt" else "--symlink")

    session.run("flit", "install", "--deps=production", *args, silent=True)


#
# Development Sessions
#
@nox.session(name="docs-live", python="3.8")
def docs_live(session):
    if session.posargs:
        docs_dir = session.posargs[0]
        additional_dependencies = session.posargs[1:]
    else:
        docs_dir = "docs/"
        additional_dependencies = ()

    boussole_command = "boussole compile --config=.boussole.json"
    _install_this_project_with_flit(session, extras=["doc"], editable=True)
    session.install("sphinx-autobuild", "boussole", *additional_dependencies)

    with tempfile.TemporaryDirectory() as destination:
        session.run(
            "sphinx-autobuild",
            # for sphinx-autobuild
            "--port=0",
            "--watch=src/",
            f"--pre-build={boussole_command}",
            r"--re-ignore=src/.*/theme/static/.*\.(css|js)",  # ignore the generated files
            "--open-browser",
            # for sphinx
            "-a",
            docs_dir,
            destination,
        )


@nox.session(python="3.8", reuse_venv=True)
def docs(session):
    _install_this_project_with_flit(session, extras=["doc"], editable=False)

    # Generate documentation into `build/docs`
    session.run("sphinx-build", "-b", "html", "-v", "docs/", "build/docs")


@nox.session(python="3.8", reuse_venv=True)
def lint(session):
    session.install("pre-commit")

    args = list(session.posargs)
    args.append("--all-files")
    if "CI" in os.environ:
        args.append("--show-diff-on-failure")

    session.run("pre-commit", "run", "--all-files", *args)


@nox.session(python="3.6")
def test(session):
    _install_this_project_with_flit(session, extras=["test"])

    args = session.posargs or ["-n", "auto", "--cov", PACKAGE_NAME]
    session.run("pytest", *args)


#
# Helpers (Release Automation)
#
def get_version_from_arguments(arguments):
    """Checks the arguments passed to `nox -s release`.

    If there is only 1 argument that looks like a version, returns the argument.
    Otherwise, returns None.
    """
    if len(arguments) != 1:
        return None

    version = arguments[0]

    parts = version.split(".")
    if len(parts) != 3:
        # Not of the form: MAJOR.MINOR.PATCH
        return None

    if not all(part.isdigit() for part in parts):
        # Not all segments are integers.
        return None

    # All is good.
    return version


def perform_git_checks(session, version_tag):
    # Ensure we're on master branch for cutting a release.
    result = subprocess.run(
        ["git", "rev-parse", "--abbrev-ref", "HEAD"],
        capture_output=True,
        encoding="utf-8",
    )
    if result.stdout != "master\n":
        session.error(f"Not on master branch: {result.stdout!r}")

    # Ensure there are no uncommitted changes.
    result = subprocess.run(
        ["git", "status", "--porcelain"], capture_output=True, encoding="utf-8"
    )
    if result.stdout:
        print(result.stdout)
        session.error("The working tree has uncommitted changes")

    # Ensure this tag doesn't exist already.
    result = subprocess.run(
        ["git", "rev-parse", version_tag], capture_output=True, encoding="utf-8"
    )
    if not result.returncode:
        session.error(f"Tag already exists! {version_tag} -- {result.stdout!r}")

    # Back up the current git reference, in a tag that's easy to clean up.
    _release_backup_tag = "auto/release-start-" + str(int(time()))
    session.run("git", "tag", _release_backup_tag, external=True)


def bump(session, *, version, file, kind):
    session.log(f"Bump version to {version!r}")
    contents = file.read_text()
    new_contents = re.sub(
        '__version__ = "(.+)"', f'__version__ = "{version}"', contents
    )
    file.write_text(new_contents)

    session.log("git commit")
    subprocess.run(["git", "add", str(file)])
    subprocess.run(["git", "commit", "-m", f"Bump for {kind}"])


#
# Release Automation
#
@nox.session
def release(session):
    release_version = get_version_from_arguments(session.posargs)
    if not release_version:
        session.error("Usage: nox -s release -- MAJOR.MINOR.PATCH")

    # Do sanity check about the state of the git repository
    perform_git_checks(session, release_version)

    # Install release dependencies
    session.install("twine", "flit")
    version_file = Path(f"src/{PACKAGE_NAME}/__init__.py")

    # Bump for release
    bump(session, version=release_version, file=version_file, kind="release")

    # Tag the release commit
    session.run(
        "git",
        "tag",
        "-s",
        "-m",
        f"Release {release_version}",
        release_version,
        external=True,
    )

    # Bump for development
    major, minor, patch = map(int, release_version.split("."))
    next_version = f"{major}.{minor}.{patch + 1}.dev0"

    bump(session, version=next_version, file=version_file, kind="development")

    # Checkout the git tag
    session.run("git", "checkout", "-q", release_version, external=True)

    # Build the distribution
    session.run("flit", "build")
    files = glob(f"dist/{PACKAGE_NAME}-{release_version}*")
    assert len(files) == 2

    # Get back out into master
    session.run("git", "checkout", "-q", "master", external=True)

    # Check and upload distribution files
    session.run("twine", "check", *files)

    # Upload the distribution
    session.run("twine", "upload", *files)

    # Push the commits and tag
    session.run("git", "push", "origin", "master", release_version, external=True)
