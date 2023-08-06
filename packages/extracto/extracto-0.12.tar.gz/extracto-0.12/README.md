# extracto

[![PyPI](https://img.shields.io/pypi/v/extracto.svg)](https://pypi.org/project/extracto/)
[![Changelog](https://img.shields.io/github/v/release/cldellow/extracto?include_prereleases&label=changelog)](https://github.com/cldellow/extracto/releases)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/cldellow/extracto/blob/main/LICENSE)

Extract Python structures from HTML files, fast.

Built on the very fast [selectolax](https://github.com/rushter/selectolax) library,
and applies a few tricks to make your life happier.

## Installation

Install this library using `pip`:

    pip install extracto

## Usage

`extracto` supports two modes: **extract** and **infer**.

**extract** mode takes an HTML document and a recipe to convert that HTML document into a Python data structure.

**infer** mode takes an HTML document and its desired output, and tries to propose a good recipe. You don't need to use infer mode at all; it's just a handy shortcut.

You can infer/extract two shapes of data:
- tabular data, as a list of lists (eg: `[['Alfie', 1986], ['Lily', 1985]]`)
- shaped data, eg `[ { 'name': 'Alfie', 'year': 1986 }, { 'name': 'Lily', 'year': 1985 }]`

Tabular data is the lowest-level layer of the system. Shaped data is built on top of tabular data.

### extract

#### Table data

```python
from extracto import prepare, extract_table
from selectolax.parser import HTMLParser

html = '''
<h1>Famous Allens</h1>
<div data-occupation="actor">
  <div><b>Name</b> Alfie</div>
  <div><b>Year</b> 1986</div>
</div>
<div data-occupation="singer">
  <div><b>Name</b> Lily</div>
  <div><b>Year</b> 1985</div>
</div>
<div data-occupation="pharmaceutical-entrepreneur">
  <div><b>Name</b> Tim</div>
  <div><b>Year</b> Unknown</div>
</div>
'''

tree = HTMLParser(html)

# Tweak the HTML to allow easier extractions.
prepare(tree, for_infer=False)

results = extract_table(
    'http://example.com/url-of-the-page',
    tree,
    {
        # Try to emit a row for every element matched by this selector
        'selector': 'h1 ~ div',
        'columns': [
            {
                # Columns are usually evaluated relative to the row selector,
                # but you can "break out" and have an absolute value by
                # prefixing the selector with "html"
                'selector': 'html h1'
                'conversions': [
                    # Strip "Famous" by capturing only the text that follows,
                    # and assigning it to the return value ('rv') group
                    re.compile('Famous (?P<rv>.+)')
                ]
            },
            {
                'selector': '.q-name + span',
            },
            {
                'selector': '.q-year + span',
                # Convert the year to an int
                'conversions': ['int'],
                # If we fail to extract something for this column, that's OK--just emit None
                'optional': True,
            },
            {
                'conversions': [
                  # Extract the value of the "data-occupation" attribute
                  '@data-occupation',
                  # Actors are boring
                  re.compile('singer|pharmaceutical-entrepreneur'),
                ],
            }
        ]
    }
)
```

Will result in:

```
[
  [ 'Allens', 'Lily', 1985, 'singer' ],
  [ 'Allens', 'Tim', None, 'pharmaceutical-entrepreneur' ],
]
```

Note that Alfie was excluded by the regular expression filter on
occupation, which permitted only `singer` and `pharmaceutical-entrepreneur` rows
through.

#### Shaped data

```python
from extracto import prepare, extract_object
from selectolax.parser import HTMLParser

html = '''
<h1>Famous Allens</h1>
<div data-occupation="actor">
  <div><b>Name</b> Alfie</div>
  <div><b>Year</b> 1986</div>
</div>
<div data-occupation="singer">
  <div><b>Name</b> Lily</div>
  <div><b>Year</b> 1985</div>
</div>
<div data-occupation="pharmaceutical-entrepreneur">
  <div><b>Name</b> Tim</div>
  <div><b>Year</b> Unknown</div>
</div>
'''

tree = HTMLParser(html)

# Tweak the HTML to allow easier extractions.
prepare(tree, for_infer=False)

results = extract_object(
    'http://example.com/url-of-the-page',
    tree,
    {
        'label': {
          '$row': 'html',
          '$column': 'h1'
        },
        'people': {
            '$': {
                '$row': '[data-occupation]',
                'name': {
                    '$column': '.q-name + span'
                },
                'year': {
                    '$column': '.q-year + span',
                    '$conversions': ['int']
                },
                'job': {
                    '$column': '[data-occupation]',
                    'conversions': ['@data-occupation']
                }
            }
        }
    }
)
```

Will give:

```
{
    "label": "Famous Allens",
    "people": [
        {
            "name": "Alfie",
            "year": 1986,
            "job": "actor"
        },
        {
            "name": "Lily",
            "year": 1985,
            "job": "singer"
        }
    ]
}
```

### infer

#### Table data

```python
from selectolax.parser import HTMLParser
from extracto import prepare, infer_table

html = '''
<h1>Famous Allens</h1>
<div data-occupation="actor">
  <div><b>Name</b> Alfie</div>
  <div><b>Year</b> 1986</div>
</div>
<div data-occupation="singer">
  <div><b>Name</b> Lily</div>
  <div><b>Year</b> 1985</div>
</div>
<div data-occupation="pharmaceutical-entrepreneur">
  <div><b>Name</b> Tim</div>
  <div><b>Year</b> Unknown</div>
</div>
'''


tree = HTMLParser(html)
prepare(tree)

recipe = infer_table(
    'http://example.com/url-of-page',
    tree,
    [
        ['Alfie', '1986'],
        ['Lily', '1985']
    ]
)
```

## Development

To contribute to this library, first checkout the code. Then create a new virtual environment:

    cd extracto
    python -m venv venv
    source venv/bin/activate

Now install the dependencies and test dependencies:

    pip install -e '.[test]'

To run the tests:

    pytest
