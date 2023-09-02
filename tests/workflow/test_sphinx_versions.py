"""Test builds against different versions of Sphinx."""

import subprocess
import venv
from pathlib import Path
from typing import Iterable

import httpx
import pytest
import tomli
from packaging.requirements import Requirement
from packaging.version import Version

REPO_ROOT_DIR = Path(__file__).parent.parent.parent


def determine_matching_sphinx_versions() -> Iterable[str]:
    # Determine the compatibility declared in pyproject.toml
    pyproject_toml = (REPO_ROOT_DIR / "pyproject.toml").read_text()

    parsed = tomli.loads(pyproject_toml)
    for dependency in parsed["project"]["dependencies"]:
        if dependency.lower().startswith("sphinx "):
            break
    else:
        raise RuntimeError("No Sphinx dependency found in pyproject.toml")

    # Determine the Sphinx versions that are available on PyPI
    response = httpx.get(
        "https://pypi.org/simple/sphinx/",
        headers={"Accept": "application/vnd.pypi.simple.v1+json"},
    )
    response.raise_for_status()
    all_sphinx_versions = [Version(v) for v in response.json()["versions"]]

    # Filter according to the declared compatibility
    matching_versions = Requirement(dependency).specifier.filter(all_sphinx_versions)

    # Determine the latest version of each minor release
    latest_minor_versions = {}
    for version in matching_versions:
        minor_for_this = version.release[:2]
        if minor_for_this not in latest_minor_versions:
            latest_minor_versions[minor_for_this] = version
        elif version > latest_minor_versions[minor_for_this]:
            latest_minor_versions[minor_for_this] = version

    yield from map(str, sorted(latest_minor_versions.values()))


@pytest.mark.parametrize("sphinx_version", determine_matching_sphinx_versions())
def test_builds_with_sphinx_version(tmp_path: Path, sphinx_version: str) -> None:
    # GIVEN
    docs_output_dir = tmp_path / "build"
    venv_dir = tmp_path / "venv"
    builder = venv.EnvBuilder(with_pip=True)

    context = builder.ensure_directories(venv_dir)
    builder.create(venv_dir)

    subprocess.run(
        [
            context.env_exe,
            "-m",
            "pip",
            "install",
            "--disable-pip-version-check",
            f"sphinx=={sphinx_version}",
        ],
        check=True,
    )
    subprocess.run(
        [
            # fmt: off
            context.env_exe,
            "-m",
            "pip",
            "install",
            "--disable-pip-version-check",
            "-e", ".",
            "-r", "docs/requirements.txt",
            # fmt: on
        ],
        check=True,
        cwd=REPO_ROOT_DIR,
    )

    # WHEN
    subprocess.run(
        [
            context.env_exe,
            "-m",
            "sphinx",
            "-b=dirhtml",
            "docs/",
            docs_output_dir,
        ],
        check=True,
        cwd=REPO_ROOT_DIR,
    )

    # THEN
    subprocess.run(["tree", docs_output_dir], check=False)
    assert (docs_output_dir / "index.html").exists()
