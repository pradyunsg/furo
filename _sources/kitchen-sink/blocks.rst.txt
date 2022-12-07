..
   Copyright (c) 2021 Pradyun Gedam
   Licensed under Creative Commons Attribution-ShareAlike 4.0 International License
   SPDX-License-Identifier: CC-BY-SA-4.0

======
Blocks
======

Block Quotes
============

Block quotes consist of indented body elements:

    My theory by A. Elk.  Brackets Miss, brackets.  This theory goes
    as follows and begins now.  All brontosauruses are thin at one
    end, much much thicker in the middle and then thin again at the
    far end.  That is my theory, it is mine, and belongs to me and I
    own it, and what it is too.

    -- Anne Elk (Miss)

Epigraph
--------

https://docutils.sourceforge.io/docs/ref/rst/directives.html#epigraph

.. epigraph::

    My theory by A. Elk.  Brackets Miss, brackets.  This theory goes
    as follows and begins now.  All brontosauruses are thin at one
    end, much much thicker in the middle and then thin again at the
    far end.  That is my theory, it is mine, and belongs to me and I
    own it, and what it is too.

    -- Anne Elk (Miss)

Pull quotes
-----------

https://docutils.sourceforge.io/docs/ref/rst/directives.html#pull-quote

.. pull-quote::

    My theory by A. Elk.  Brackets Miss, brackets.  This theory goes
    as follows and begins now.  All brontosauruses are thin at one
    end, much much thicker in the middle and then thin again at the
    far end.  That is my theory, it is mine, and belongs to me and I
    own it, and what it is too.

    -- Anne Elk (Miss)

Highlights
----------

https://docutils.sourceforge.io/docs/ref/rst/directives.html#highlights

.. highlights::

    My theory by A. Elk.  Brackets Miss, brackets.  This theory goes
    as follows and begins now.  All brontosauruses are thin at one
    end, much much thicker in the middle and then thin again at the
    far end.  That is my theory, it is mine, and belongs to me and I
    own it, and what it is too.

    -- Anne Elk (Miss)

Line Blocks
===========

https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#line-blocks

This is a normal text paragraph.

| This is a line block.  It ends with a blank line.
|     Each new line begins with a vertical bar ("|").
|     Line breaks and initial indents are preserved.
| Continuation lines are wrapped portions of long lines;
  they begin with a space in place of the vertical bar.
|     The left edge of a continuation line need not be aligned with
  the left edge of the text above it.

| This is a second line block.
|
| Blank lines are permitted internally, but they must begin with a "|".

This is a normal text paragraph again.

Monospace Blocks
================

Sphinx supports many kinds of monospace blocks. This section is meant to
showcase *all* of them that as known to the author of this page, at the time of
writing.

Production List
---------------

https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-productionlist

    This directive is used to enclose a group of productions. Each production is given on a single line and consists of a name, separated by a colon from the following definition.

This just shows up as a vanilla ``<pre>``, which is... both nice and a bit
annoying.

.. productionlist::
    try_stmt: try1_stmt | try2_stmt
    try1_stmt: "try" ":" `suite`
             : ("except" [`expression` ["," `target`]] ":" `suite`)+
             : ["else" ":" `suite`]
             : ["finally" ":" `suite`]
    try2_stmt: "try" ":" `suite`
             : "finally" ":" `suite`
             : "this-is-intentionally-very-stupidly-long-to-make-sure-that-this-has-a-proper-scrollbar"

Literal Blocks
--------------

https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#literal-blocks

    contains a block of text where line breaks and whitespace are significant and must be preserved

This is a normal text paragraph. The next paragraph is a code sample::

    It is not processed in any way, except
    that the indentation is removed.

    It can span multiple lines.

This is a normal text paragraph again.

They can be quoted without indentation::

>> Great idea!
>
> Why didn't I think of that?

.. literalinclude:: ../../src/furo/__init__.py
    :language: python
    :caption: Literal includes can also have captions.
    :linenos:
    :lines: 10-20

Doctest Blocks
--------------

https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#doctest-blocks

    Doctest blocks are interactive Python sessions cut-and-pasted into docstrings. They are meant to illustrate usage by example, and provide an elegant and powerful testing environment via the doctest module in the Python standard library.

.. note::

    This is fine.

>>> print('Python-specific usage examples; begun with ">>>"')
Python-specific usage examples; begun with ">>>"
>>> print("(cut and pasted from interactive Python sessions)")
(cut and pasted from interactive Python sessions)
>>> print("This is an intentionally very long line because I want to make sure that we are handling scrollable code blocks correctly.")
This is an intentionally very long line because I want to make sure that we are handling scrollable code blocks correctly.

Parsed Literals
---------------

https://docutils.sourceforge.io/docs/ref/rst/directives.html#parsed-literal-block

    It is equivalent to a line block with different rendering: typically in a typewriter/monospaced typeface, like an ordinary literal block. Parsed literal blocks are useful for adding hyperlinks to code examples.

.. parsed-literal::

    # parsed-literal test
    curl -O http://someurl/release-0.1.0.tar-gz
    echo "This is an intentionally very long line because I want to make sure that we are handling scrollable code blocks correctly."

Code Block
----------

https://docutils.sourceforge.io/docs/ref/rst/directives.html#code

    The "code" directive constructs a literal block [containing code].

This has an alias of ``code-block``.


.. code-block:: python
    :linenos:

    from typing import Iterator

    # This is an example
    class Math:
        @staticmethod
        def fib(n: int) -> Iterator[int]:
            """Fibonacci series up to n"""
            a, b = 0, 1
            while a < n:
                yield a
                a, b = b, a + b


    result = sum(Math.fib(42))
    print("The answer is {}".format(result))


With caption
~~~~~~~~~~~~

.. code-block:: json
    :caption: Code Blocks can have captions, which also adds a link to it.

    {
      "session_name": "shorthands",
      "windows": [
        {
          "panes": [
            {
              "shell_command": "echo 'This is an intentionally very long line because I want to make sure that we are handling scrollable code blocks correctly.'"
            }
          ],
          "window_name": "long form"
        }
      ]
    }

With line numbers
~~~~~~~~~~~~~~~~~

.. code-block:: python
    :linenos:
    :emphasize-lines: 3,5

    def some_function():
        interesting = False
        print("This line is highlighted.")
        print("This one is not...")
        print("...but this one is.")
        print(
            "This is an intentionally very long line because I want to make sure that we are handling scrollable code blocks correctly."
        )

With ``none`` highlighting
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: none

    # Taken from https://en.wikipedia.org/wiki/Pseudocode#Example
    algorithm ford-fulkerson is
        input: Graph G with flow capacity c,
            source node s,
            sink node t
        output: Flow f such that f is maximal from s to t

        (Note that f(u,v) is the flow from node u to node v, and c(u,v) is the flow capacity from node u to node v)

        for each edge (u, v) in GE do
            f(u, v) ← 0
            f(v, u) ← 0

        while there exists a path p from s to t in the residual network Gf do
            let cf be the flow capacity of the residual network Gf
            cf(p) ← min{cf(u, v) | (u, v) in p}
            for each edge (u, v) in p do
                f(u, v) ←  f(u, v) + cf(p)
                f(v, u) ← −f(u, v)

        return f
