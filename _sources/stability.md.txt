# Stability Policy

```{note}
This does not apply for beta releases of Furo.
```

Users that aren't using custom templates or undocumented details of Furo should not expect any breaking changes. For everyone else, I won't actively try to break things but that doesn't mean there won't be occasional breakage.

## Specifics

### Design tweaks

Every new release may contain a minor design tweaks or additional support for new things in Sphinx.

### Sphinx version support

Any new release may drop support for older versions of Sphinx.

### Checking for incompatible changes

The "Reference" and "Kitchen Sink" sections (of Furo's documentation) will be used prior to each release, to ensure that the theme doesn't break "normal" content.

### Documented customisations

Documented customisations will also continue to work, unless documented as unstable.

### Undocumented / "unstable" customisations

Since there is no way to ensure all possible customisations are not affected, Furo makes no promises about them -- notably, there's no stability promise around the exact filenames in the theme templates or theme assets. If you wish to define your own templates or override Furo's assets, it is recommended to be mindful of when you might get a new Furo release and it may make sense to "pin" the version of Furo.

## Reasons

Furo was largely motivated by "I want things to look nicer", when looking at pip's documentation in early 2021.

These stability promises are aimed toward keeping it straightforward for me to maintain and improve this theme going forward. Any additional overhead in keeping the project moving along, would make it less likely that I'd actually continue working on this project.

Since this project is "largely aesthetics" for nearly all end users, I'd prefer to preserve the contract to just that -- it'll look the same, with minor tweaks expected based on how the Sphinx ecosystem evolves and what I feel should be included in the theme.
