..
   Copyright (c) 2021 Pradyun Gedam
   Licensed under Creative Commons Attribution-ShareAlike 4.0 International License
   SPDX-License-Identifier: CC-BY-SA-4.0

=====
Lists
=====

Enumerated Lists
----------------

1. Arabic numerals.

   a) lower alpha)

      (i) (lower roman)

          A. upper alpha.

             I) upper roman)

2. Lists that don't start at 1:

   3. Three

   4. Four

   c. c

   d. d

   C. C

   D. D

   iii. iii

   iv. iv

   III. III

   IV. IV

#. List items may also be auto-enumerated.

Definition Lists
----------------

Term
    Definition
Term : classifier
    Definition paragraph 1.

    Definition paragraph 2.
Term
    Definition

I have no clue why the definition list below is classified as a different style
of definition list than the one above.

Is it the spaces in the term?
    Maybe it was the multiple line paragraph
    in the line below that caused this?

Is it the paragraph above the list maybe?
    I guess a lot of these lists don't have leading paragraphs?

Is it everything all at once?
    Who knows?!

Option Lists
------------

For listing command-line options:

-a            command-line option "a"
-b file       options can have arguments
              and long descriptions
--long        options can be long also
--input=file  long options can also have
              arguments

--very-long-option
              The description can also start on the next line.

              The description may contain multiple body elements,
              regardless of where it starts.

-x, -y, -z    Multiple options are an "option group".
-v, --verbose  Commonly-seen: short & long options.
-1 file, --one=file, --two file
              Multiple options with arguments.
/V            DOS/VMS-style options too

There must be at least two spaces between the option and the description.

Field list
----------

:Address: 123 Example Street
          Example, EX  Canada
          A1B 2C3
:Organization: humankind
:Status: This is a "work in progress"
:Version: 1
:Field name: This is a generic bibliographic field.
:Field name 2:
    Generic bibliographic fields may contain multiple body elements.

    Like this.

Glossary
--------

This is a glossary with definition terms for thing like :term:`Writing`:

.. glossary::

  Documentation
     Provides users with the knowledge they need to use something.

  Reading
     The process of taking information into ones mind through the use of eyes.

  Writing
     The process of putting thoughts into a medium for other people to :term:`read <Reading>`.

Here's another glossary, with more detail. The important bit here is that the contents of the definition are multi-paragraph.

.. glossary::

    Import Package

        A Python module which can contain other modules or recursively, other packages.

        An import package is more commonly referred to with the single word “package”, but this guide will use the expanded term when more clarity is needed to prevent confusion with a Distribution Package which is also commonly called a “package”.

    Package Index

        A repository of distributions with a web interface to automate package discovery and consumption.

Bullet Lists
------------

..
    Docutils supports two types of lists, "simple" and "complex". Complex lists
    have item margins, simple lists do not.
    https://docutils.sourceforge.io/sandbox/html4strict/data/simple-lists.html

Simple
^^^^^^

- A simple list.
- There are no margins between list items.
- Simple lists do not contain multiple paragraphs. That's a complex list.
- In the case of a nested list

  - There are no margins between elements

    - Still no margins

      - Still no margins

Complex
^^^^^^^

- A bullet list

  + Nested bullet list.
  + Nested item 2.

- Item 2.

  Paragraph 2 of item 2.

  * Nested bullet list.
  * Nested item 2.

    - Third level.
    - Item 2.

  * Nested item 3.

- ``inline literall``
- ``inline literall``
- ``inline literall``
- This item has multiple paragraphs.

  This item has multiple paragraphs.
- This item has multiple paragraphs.

  This item has multiple paragraphs.


Second list level
^^^^^^^^^^^^^^^^^

- here is a list in a second-level section.
- `yahoo <http://www.yahoo.com>`_
- `yahoo <http://www.yahoo.com>`_

  - `yahoo <http://www.yahoo.com>`_
  - here is an inner bullet ``oh``

    - one more ``with an inline literally``. `yahoo <http://www.yahoo.com>`_

      heh heh. child. try to beat this embed:

      .. literalinclude:: ../../src/furo/__init__.py
          :language: python
          :linenos:
          :lines: 10-20

  - and another. `yahoo <http://www.yahoo.com>`_
  - `yahoo <http://www.yahoo.com>`_
  - ``hi``
- how about an admonition?

  .. note::
      This is a note nested in a list.

- and hehe

But deeper down the rabbit hole
"""""""""""""""""""""""""""""""

- I kept saying that, "deeper down the rabbit hole". `yahoo <http://www.yahoo.com>`_

  - I cackle at night `yahoo <http://www.yahoo.com>`_.
- I'm so lonely here in GZ ``guangzhou``
- A man of python destiny, hopes and dreams. `yahoo <http://www.yahoo.com>`_

  - `yahoo <http://www.yahoo.com>`_

    - `yahoo <http://www.yahoo.com>`_ ``hi``
    - ``destiny``

Hlists
------

.. hlist::
    :columns: 2

    - First item
    - Second item
    - Third item
    - Forth item
    - Fifth item
    - Sixths item

.. rubric:: Hlist with images

.. hlist::
    :columns: 2

    - .. figure:: https://source.unsplash.com/200x200/daily?cute+puppy

         This is a short caption for a figure.

    - .. figure:: https://source.unsplash.com/200x200/daily?cute+puppy

         This is a long caption for a figure. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
         Donec porttitor dolor in odio posuere, vitae ornare libero mattis. In lobortis justo vestibulum nibh aliquet, non.

Numbered List
-------------

#. One,
#. Two.
#. Three with long text. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
   Sed feugiat sagittis neque quis eleifend. Duis rutrum lectus sit amet mattis suscipit.

- A) Using bullets and letters. (A)
- B) Using bullets and letters. (B)
- C) Using bullets and letters. (C)
