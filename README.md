Thumbor Tex Filter
===

This plugins provide a way to generate text via Thumbor Filter.

## Installation
`pip install thumbor_text_filter`

## Configuration

By adding `FILTERS` in `thumbor.conf` with `thumbor_text_filter`, for example:
```
FILTERS =     [
    # other filters....
    'thumbor_text_filter',
]
```

## Usage
Add `text()` to thumbor url at `filters` section, method signature is like this:

`text(word, x, y, color, font-size, font-family)`

You can omit `font-family`, it will use `Tahoma` as default.
For `color`, please see available color here http://pillow.readthedocs.io/en/4.0.x/reference/ImageColor.html#color-names

Here'are some examples:
```
http://thumbor/unsafe/filter:text(hello,10,10,red,25)/your-image-url
http://thumbor/unsafe/filter:text(hello,10,10,red,25,Arial)/your-image-url
```

---
## Copyright
MIT