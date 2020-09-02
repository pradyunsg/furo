"""Development automation
"""
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
@nox.session(name="docs-live", python="3.8")
def docs_live(session):
    if session.posargs:
        docs_dir = session.posargs[0]
        additional_dependencies = session.posargs[1:]
    else:
        docs_dir = "docs/"
        additional_dependencies = ()

    build_command = "gulp build"
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
