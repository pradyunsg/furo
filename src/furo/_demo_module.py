# Copyright (c) 2021 Pradyun Gedam
# SPDX-License-Identifier: MIT

"""This is a demo module included in the docs in order to exercise autodoc."""

from typing import Optional, TextIO, Type, Union


def show_warning(
    message: Union[Warning, str],
    category: Type[Warning],
    filename: str,
    lineno: int,
    file: Optional[TextIO] = None,
    line: Optional[str] = None,
) -> None:
    """Show a warning to the end user.

    .. code:: python

        warnings.showwarning = show_warning

    :param message: What you want to tell the user.
    :param category: The type of warning.
    :param filename: The file that the warning is for.
    :param lineno: The line that the warning is for.
    :param file: Where to write the warning.
    :param line: line of source code to be included in the warning message
    """


class RandomNumberGenerator:
    """A random number generator."""

    def __init__(self, *, seed: int = 4) -> None:
        """Initialize."""
        self._seed = 4

    @property
    def seed(self) -> int:
        """Get seed for random number generation.

        .. versionadded:: 1.0

        .. versionchanged:: 1.1
            Use ``random`` to create the seed.

        .. deprecated:: 1.2
            ``random`` raises security concerns.

        .. versionremoved:: 1.3
            ``random`` replaced with a random number.

        .. seealso:: https://xkcd.com/221/
        """
        return self._seed

    def get_random_integer(self) -> int:
        """Return a random integer."""
        return self.seed

    def get_random_float(self) -> float:
        """Return a random float."""
        return float(self.seed)


def annoying_function_name_length_aa(one: int, two: int) -> str:
    """Add two numbers as strings.

    Because I needed a placeholder function.
    """
    return str(one) + str(two)


def annoying_function_name_length_aaa(one: int, two: int) -> str:
    """Add two numbers as strings.

    Because I needed a placeholder function.
    """
    return str(one) + str(two)
