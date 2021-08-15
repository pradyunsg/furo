# Tabs

Tabs are good way to organize content, where the reader has choice they can make (usually based on their environment).

While Sphinx does not provide tabs out-of-the-box, it is achievable by using extensions with Sphinx. Furo works well with the following extensions.

## [sphinx-inline-tabs]

This is a small package that provides one thing: good-looking tabs that work.

````{furo-demo}

```{tab} One
First.
```

```{tab} Two
Second.
```

+++

.. tab:: One

    First.

.. tab:: Two

    Second.

````

## [sphinx-design]

A wide ranging extension, providing many reusable components for site content, including tabs.

`````{furo-demo}

````{tab-set}
```{tab-item} Label1
Markdown 1
```

```{tab-item} Label2
Markdown 2
```
````

+++

.. tab-set::

    .. tab-item:: Label1

        reStructuredText 1

    .. tab-item:: Label2

        reStructuredText 2

`````

[sphinx-inline-tabs]: https://github.com/pradyunsg/sphinx-inline-tabs#readme
[sphinx-design]: https://sphinx-design.readthedocs.io/en/furo-theme/
