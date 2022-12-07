# sphinx-design stuff

## Icons

{octicon}`heart-fill;1em;sd-text-danger`

## Tabs

````{tab-set}
```{tab-item} Label1
Markdown 1
```

```{tab-item} Label2
Markdown 2
```
````

## Dropdowns

```{dropdown}
Dropdown content
```

```{dropdown} Dropdown title
Dropdown content
```

```{dropdown} Open dropdown
:open:

Dropdown content
```

## Shadows

```{dropdown} Default Shadow
Dropdown content
```

```{dropdown} "sm" Shadow
:class-container: sd-shadow-sm

Dropdown content
```

```{dropdown} "md" Shadow
:class-container: sd-shadow-md

Dropdown content
```

```{dropdown} "lg" Shadow
:class-container: sd-shadow-lg

Dropdown content
```

## Cards

```{card} Card Title
Header
^^^
Card content
+++
Footer
```

```{card} Clickable Card (external)
:link: https://example.com

The entire card can be clicked to navigate to <https://example.com>.
```

## Grid Cards

This also checks the interaction of only-dark and only-light.

````{grid} 1 1 2 3
```{grid-item-card} One
:img-top: https://via.placeholder.com/700.png?text=One
:link: https://example.com/
```

```{grid-item-card} Two (only-dark)
:img-top: https://via.placeholder.com/700.png/000000/FFFFFF/?text=only-dark
:link: https://example.com/
:class-item: only-dark
```

```{grid-item-card} Two (only-light)
:img-top: https://via.placeholder.com/700.png/FFFFFF/000000?text=only-light
:link: https://example.com/
:class-item: only-light
```

```{grid-item-card} Three
:img-top: https://via.placeholder.com/700.png?text=Three
:link: https://example.com/
```
````

## Carousels

````{card-carousel} 2

```{card} card 1
```

```{card} card 2
```

```{card} card 3
```

```{card} card 4
```

```{card} card 5
```

```{card} card 6
```

````

## Article Info

```{article-info}
:avatar: https://avatars.githubusercontent.com/u/3275593?s=80&v=4
:avatar-link: https://pradyunsg.me
:avatar-outline: muted
:author: Pradyun Gedam
:date: Aug 15, 2021
:read-time: 5 min read
```

## Badges

{bdg}`plain badge`

{bdg-primary}`primary` {bdg-primary-line}`primary-line`

{bdg-secondary}`secondary` {bdg-secondary-line}`secondary-line`

{bdg-success}`success` {bdg-success-line}`success-line`

{bdg-info}`info` {bdg-info-line}`info-line`

{bdg-warning}`warning` {bdg-warning-line}`warning-line`

{bdg-danger}`danger` {bdg-danger-line}`danger-line`

{bdg-light}`light` {bdg-light-line}`light-line`

{bdg-dark}`dark` {bdg-dark-line}`dark-line`

## Buttons

```{button-link} https://example.com
Button text
```

```{button-link} https://example.com
:color: primary
Button text
```

```{button-link} https://example.com
:color: secondary
:expand:
```
