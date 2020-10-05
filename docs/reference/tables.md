# Tables

Tables can be the best way to organize sets of related pieces of data. Sphinx supports including tables inline, although the exact syntax and capabilities depend on the markup language used.

````{furo-demo}

MyST supports tables like [GitHub Flavoured Markdown][1].

| Header  | Another header |
|---------|----------------|
| field 1 | something      |
| field 2 | something else |

List tables are also a thing:

```{list-table}
:header-rows: 1

* - This is
  - the header
  - row
* - First
  - row of
  - very important content
* - Second
  - row of
  - very important content
```

[1]: https://docs.github.com/en/github/writing-on-github/organizing-information-with-tables

+++

Grid table:

+------------+------------+-----------+
| Header 1   | Header 2   | Header 3  |
+============+============+===========+
| body row 1 | column 2   | column 3  |
+------------+------------+-----------+
| body row 2 | Cells may span columns.|
+------------+------------+-----------+
| body row 3 | Cells may  | - Cells   |
+------------+ span rows. | - contain |
| body row 4 |            | - blocks. |
+------------+------------+-----------+

Simple table:

=====  =====  ======
   Inputs     Output
------------  ------
  A      B    A or B
=====  =====  ======
False  False  False
True   False  True
False  True   True
True   True   True
=====  =====  ======

````
