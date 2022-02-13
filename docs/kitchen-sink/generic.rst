..
   Copyright (c) 2021 Pradyun Gedam
   Licensed under Creative Commons Attribution-ShareAlike 4.0 International License
   SPDX-License-Identifier: CC-BY-SA-4.0

.. |EXAMPLE| image:: https://source.unsplash.com/32x32/daily?icon
    :width: 1em

=============
Generic items
=============

These are the things that don't quite fit into other groupings.

Inline Markup
=============

One of the nice things about markup languages is the ability to have inline
markup. This makes the presentation *much* nicer. The **bold** text shouldn't
be too overbearing. It is very common to have ``inline code`` as well. It is
important to ensure that the inline code doesn't have a line height that is
greater than the regular prose; otherwise the spacing looks weird.

It is also possible to use explicit roles to do things like a :sub:`subscript`,
a :sup:`superscript`, :emphasis:`emphasis`, :strong:`strong`, and
:literal:`literal`.

Hyperlinks
----------

It is a website, so it'll have hyperlinks like http://www.python.org (inline),
or Python_ (external reference), example_ (internal reference),
`Python web site <http://www.python.org>`__ (external hyperlinks with embedded
URI), footnote references (manually numbered [1]_, anonymous auto-numbered [#]_,
labeled auto-numbered [#label]_, or symbolic [*]_), citation references ([12]_),
substitution references (|example|), and _`inline hyperlink targets`
(see Targets_ below for a reference back to here).

reStructuredText has character-level inline markup too. It's ugly to write, but
someone might be using it, so here's an example: **re**\ ``Structured``\ *Text*.

It is also possible to link to documented items, such as
:class:`api_sample.RandomNumberGenerator`.

Interpreted text
----------------

The default role for "interpreted text" (AKA single backticks) is
`Title Reference`. There are other reference syntaxes as well: :PEP:`287` and
:RFC:`2822`.

If the ``--pep-references`` option was supplied, there should be a live link to
PEP 258 here.

GUI labels
^^^^^^^^^^

According to the RST demo, GUI labels (like :guilabel:`this label`) are a way to
indicate that some action is to be taken by the user. Like inline code literals,
GUI labels should not run over line height.

Keys / Menu labels
^^^^^^^^^^^^^^^^^^

Key-bindings indicate that the read is to press a button on the keyboard or
mouse, for example :kbd:`MMB`, :kbd:`⌘+⇧+M` and :kbd:`Shift-MMB`. Another
useful way is ``menuselection`` to show menus:
:menuselection:`My --> Software --> Some menu --> Some sub menu 1 --> Some sub menu 2 --> Some sub menu 3`

For example, ``menuselection`` should break when it is too long to fit on a
single line.

Long inline code wrapping
^^^^^^^^^^^^^^^^^^^^^^^^^

.. DO NOT RE-WRAP THE FOLLOWING PARAGRAPH!

Let's test wrapping and whitespace significance in inline literals:
``This is an example of --inline-literal --text, --including some--
strangely--hyphenated-words.  Adjust-the-width-of-your-browser-window
to see how the text is wrapped.  -- ---- --------  Now note    the
spacing    between the    words of    this sentence    (words
should    be grouped    in pairs).``

Math
====

This is a test. Here is an equation:
:math:`X_{0:5} = (X_0, X_1, X_2, X_3, X_4)`.
Here is another:

.. math::
    :label: This is a label

    \nabla^2 f =
    \frac{1}{r^2} \frac{\partial}{\partial r}
    \left( r^2 \frac{\partial f}{\partial r} \right) +
    \frac{1}{r^2 \sin \theta} \frac{\partial f}{\partial \theta}
    \left( \sin \theta \, \frac{\partial f}{\partial \theta} \right) +
    \frac{1}{r^2 \sin^2\theta} \frac{\partial^2 f}{\partial \phi^2}

You can add a link to equations like the one above :eq:`This is a label` by using
``:eq:``.


Sidebar
=======

.. sidebar:: Ch'ien / The Creative

    Lorem ipsum dolor sit amet consectetur adipisicing elit.

    .. image:: https://source.unsplash.com/200x200/daily?cute+puppy

    Lorem ipsum dolor sit amet consectetur adipisicing elit.

Lorem ipsum dolor sit amet consectetur adipisicing elit. Accusamus, sunt
voluptatum tenetur libero nulla esse veritatis accusantium earum commodi hic
voluptatem officia culpa optio atque. Quaerat sed quibusdam ratione nam.

Lorem ipsum dolor sit amet consectetur adipisicing elit. Accusamus, sunt
voluptatum tenetur libero nulla esse veritatis accusantium earum commodi hic
voluptatem officia culpa optio atque. Quaerat sed quibusdam ratione nam.

Code with Sidebar
-----------------

.. sidebar:: A code example

    With a sidebar on the right.

.. code-block:: python
    :caption: Code blocks can also have captions.
    :linenos:

    print("one")
    print("two")
    print("three")
    print("four")
    print("five")
    print("six")
    print("seven")
    print("eight")
    print("nine")
    print("ten")
    print("eleven")
    print("twelve")
    print("thirteen")
    print("fourteen")

References
==========

Footnotes
---------

.. [1] A footnote contains body elements, consistently indented by at
   least 3 spaces.

   This is the footnote's second paragraph.

.. [#label] Footnotes may be numbered, either manually (as in [1]_) or
   automatically using a "#"-prefixed label.  This footnote has a
   label so it can be referred to from multiple places, both as a
   footnote reference ([#label]_) and as a hyperlink reference
   (label_).

.. [#] This footnote is numbered automatically and anonymously using a
   label of "#" only.

.. [*] Footnotes may also use symbols, specified with a "*" label.
   Here's a reference to the next footnote: [*]_.

.. [*] This footnote shows the next symbol in the sequence.

Citations
---------

.. [12] This citation has some ``code blocks`` in it, maybe some **bold** and
       *italics* too. Heck, lets put a link to a meta citation [13]_ too.

.. [13] This citation will have one backlink.

Here's a reference to the above, [12]_ citation.

Here is another type of citation: `citation`

Targets
-------

.. _example:

This paragraph is pointed to by the explicit "example" target.
A reference can be found under `Inline Markup`_, above. `Inline
hyperlink targets`_ are also possible.

Section headers are implicit targets, referred to by name. See
Targets_.

Explicit external targets are interpolated into references such as "Python_".

.. _Python: http://www.python.org/

Targets may be indirect and anonymous.  Thus `this phrase`__ may also
refer to the Targets_ section.

__ Targets_

Target Footnotes
----------------

.. target-notes::

Centered text
=============

You can create a statement with centered text with ``.. centered::``

.. centered:: This is centered text!

Rubric
======

  A rubric is like an informal heading that doesn't correspond to the document's structure.

  -- https://docutils.sourceforge.io/docs/ref/rst/directives.html#rubric

Wikipedia says it is something different:

  A rubric is a word or section of text that is traditionally written or printed in red ink for emphasis.

  -- https://en.wikipedia.org/wiki/Rubric

This is stylized as docutils tells us to stylize it, since it is used for footnote headers (see end of https://docs.python.org/3/reference/lexical_analysis.html)

.. rubric:: This is a rubric

Sidebars and Rubrics
--------------------

.. sidebar:: Sidebar Title
   :subtitle: Optional Subtitle

   This is a sidebar.  It is for text outside the flow of the main
   text.

   .. rubric:: This is a rubric inside a sidebar

   Sidebars often appears beside the main text with a border and
   background color.

Lorem ipsum dolor sit amet consectetur adipisicing elit. Accusamus, sunt
voluptatum tenetur libero nulla esse veritatis accusantium earum commodi hic
voluptatem officia culpa optio atque. Quaerat sed quibusdam ratione nam.

Lorem ipsum dolor sit amet consectetur adipisicing elit. Accusamus, sunt
voluptatum tenetur libero nulla esse veritatis accusantium earum commodi hic
voluptatem officia culpa optio atque. Quaerat sed quibusdam ratione nam.

Lorem ipsum dolor sit amet consectetur adipisicing elit. Accusamus, sunt
voluptatum tenetur libero nulla esse veritatis accusantium earum commodi hic
voluptatem officia culpa optio atque. Quaerat sed quibusdam ratione nam.

Lorem ipsum dolor sit amet consectetur adipisicing elit. Accusamus, sunt
voluptatum tenetur libero nulla esse veritatis accusantium earum commodi hic
voluptatem officia culpa optio atque. Quaerat sed quibusdam ratione nam.

Download Links
==============

:download:`This long long long long long long long long long long long long long long long download link should wrap white-spaces <https://source.unsplash.com/200x200/daily?cute+puppy>`
