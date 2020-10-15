"""Development automation
"""
import datetime
import glob
import os
import tempfile

import nox

PACKAGE_NAME = "furo"
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
@nox.session(name="docs-live", python="3.8", reuse_venv=True)
def docs_live(session):
    if session.posargs:
        docs_dir = session.posargs[0]
        additional_dependencies = session.posargs[1:]
    else:
        docs_dir = "docs/"
        additional_dependencies = ()

    build_command = "./node_modules/.bin/gulp build"
    _install_this_project_with_flit(session, extras=["doc"], editable=True)
    session.install("sphinx-autobuild", *additional_dependencies)

    with tempfile.TemporaryDirectory() as destination:
        session.run(
            "sphinx-autobuild",
            # for sphinx-autobuild
            "--port=0",
            "--watch=src/",
            f"--pre-build={build_command}",
            r"--re-ignore=src/.*/theme/static/.*\.(css|js)",  # ignore the generated files
            "--open-browser",
            # for sphinx
            "-b=dirhtml",
            "-a",
            docs_dir,
            destination,
        )


@nox.session(python="3.8", reuse_venv=True)
def docs(session):
    # Generate relevant files prior to installation
    session.run("gulp", "build", external=True)

    _install_this_project_with_flit(session, extras=["doc"], editable=False)

    # Generate documentation into `build/docs`
    session.run("sphinx-build", "-b", "dirhtml", "-v", "docs/", "build/docs")


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


def get_release_versions(version_file):
    marker = "__version__ = "

    with open(version_file) as f:
        for line in f:
            if line.startswith(marker):
                version = line[len(marker) + 1 : -2]
                current_number = int(version.split(".dev")[-1])
                break
        else:
            raise RuntimeError("Could not find current version.")

    today = datetime.date.today()
    release_version = today.strftime(f"%Y.%m.%d.beta{current_number}")
    next_version = today.strftime(f"%Y.%m.%d.dev{current_number+1}")

    return release_version, next_version


@nox.session
def release(session):
    version_file = f"src/{PACKAGE_NAME}/__init__.py"
    allowed_upstreams = [
        f"git@github.com:pradyunsg/{PACKAGE_NAME.replace('_', '-')}.git"
    ]

    release_version, next_version = get_release_versions(version_file)

    session.install("flit", "twine", "release-helper")

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
    session.run("flit", "build")
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
