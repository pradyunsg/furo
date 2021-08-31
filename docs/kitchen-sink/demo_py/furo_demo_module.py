"""
This is a demo module included in the docs in order to exercise viewcode,
autodoc, and other related functionality.
"""

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

    :param message: What you want to tell the user.
    :param category: The type of warning.
    :param filename: The file that the warning is for.
    :param lineno: The line that the warning is for.
    :param file: Where to write the warning.
    :param line: line of source code to be included in the warning message
    """


class RandomNumberGenerator:
    """A random number generator.

    You can use this as follows.

    .. code-block:: python

       RNG = RandomNumberGenerator()
       print(RNG.get_random_integer())

    This is hopefully useful to somebody.
    """

    @property
    def seed(self):
        """The seed for random number generation.

        .. seealso:: https://xkcd.com/221/
        """
        return 4

    def get_random_integer(self) -> int:
        """Return a random integer."""
        return self.seed

    def get_random_float(self) -> float:
        """Return a random float."""
        return float(self.seed)
