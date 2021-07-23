"""
This is a demo module included in the docs in order to exercise viewcode,
autodoc, and other related functionality.
"""


class Foo:
    """
    A demo class of type Foo.

    Has a method baz() returning ints.
    """

    def baz(self) -> int:
        """
        Return a random integer.
        See also: https://xkcd.com/221/
        """
        return 3


def bar(f: Foo) -> Foo:
    """
    the identity function, but only for Foos
    """
    if isinstance(f, Foo):
        return f
    raise TypeError("Expected a Foo!")
