# dictpath_resolver

[![PyPI Version][pypi-version]][pypi-url]
[![PyPI Downloads][pypi-downloads]][pypi-url]

[pypi-version]: https://img.shields.io/pypi/v/dictpath_resolver
[pypi-url]: https://pypi.org/project/dictpath_resolver/
[pypi-downloads]: https://img.shields.io/pypi/dm/dictpath_resolver

Provides a simple syntax to access nested JSON-like object in python.

## Syntax

The path should be a string, which consists of recurring patterns:

    Patern1Patern2Patern3......

There are 2 types of paterns:

- Dict member access patern: Starts with `.` then follows the member name. Member name must contain only `/a-zA-Z\d\-_/`.
- List item access patern: has an integer inside brackets `[]`.

Paterns are evaluated first, then applied recursively to current child object,
final value would be return when the list is exhausted.

Example:
```
object: {"building": {"floors": [{"name": "A"}, {"name": "B"}, {"name": "C"}]}}
path: ".building.floors[1].name"
resolved value: "B"
```

## Usage
```python
from dictpath_resolver import DictPathResolver

json_like = {"building": {"floors": [{"name": "A"}, {"name": "B"}, {"name": "C"}]}}
path = ".building.floors[1].name"
resolver = DictPathResolver(json_like, path)

print(resolver.is_resolvable())
# True
print(resolver.resolve())
# B

```