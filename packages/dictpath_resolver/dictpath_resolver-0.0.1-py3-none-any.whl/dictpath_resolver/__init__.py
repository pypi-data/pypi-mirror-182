"""Provides a simple syntax to access nested JSON-like object in python.

The path should be a string, which consists of recurring patterns:
    Patern1Patern2Patern3......
There are 2 types of paterns:
    Dict member access patern: Starts with `.` then follows the member name. 
    Member name must contain only /a-zA-Z\d\-_/.
    List item access patern: has an integer inside brackets `[]`.
Paterns are evaluated first, then applied recursively to current child object,
final value would be return when the list is exhausted.

Example:
    object: {"building": {"floors": [{"name": "A"}, {"name": "B"}, {"name": "C"}]}}
    path: ".building.floors[1].name"
    resolved value: "B"
"""


__version__ = "0.0.1"
