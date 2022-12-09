# Code Blocks

Code blocks and examples are an essential part of technical project documentation. Sphinx provides syntax highlighting for these out-of-the-box, through Pygments.

````{furo-demo}

Code blocks in Markdown can be created in various ways.

    Indenting content by 4 spaces.
    This will not have any syntax highlighting.


```
Wrapping text with triple backticks also works.
This will have default syntax highlighting (highlighting a few words and "strings").
```

```python
print("And with the triple backticks syntax, you can have syntax highlighting.")
```

```none
print("Or disable all syntax highlighting.")
```

There's a lot of power hidden underneath the triple backticks in MyST Markdown,
as seen in <https://myst-parser.readthedocs.io/en/latest/syntax/roles-and-directives.html>.

+++

Code blocks in reStructuredText can be created in various ways::

    Indenting content by 4 spaces, after a line ends with "::".
    This will have default syntax highlighting (highlighting a few words and "strings").

.. code::

    You can also use the code directive, or an alias: code-block, sourcecode.
    This will have default syntax highlighting (highlighting a few words and "strings").

.. code:: python

    print("And with the directive syntax, you can have syntax highlighting.")

.. code:: none

    print("Or disable all syntax highlighting.")


There's a lot more forms of "blocks" in reStructuredText that can be used, as
seen in https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#literal-blocks.
````
