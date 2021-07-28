# Changing sidebar title

It is possible to have a custom sidebar title in the Sphinx documentation. This is
achieved by adding a variable to the `conf.py` file:

```py
html_title = "your custom sidebar title"
```

If `html_title` is used, then it overwrites the default sidebar title text that is:

```
<project> <release> documentation
```

where `project` and `release` are variables with the same name in the `conf.py` file.
If `release` is not specified, it will be omitted from the title.
