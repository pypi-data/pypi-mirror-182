import operator
import re
from typing import Any, Union, Callable

from exceptions import UnresolvableError


class DictPathResolver:
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

    PATH_VALIDATION_REGEX = re.compile(r"(?:\.[a-zA-Z\d\-_]+(?:\[\d+\])*)+")
    PARSE_REGEX = re.compile(r"\.([a-zA-Z\d\-_]+)|(?:\[(\d+)\])")

    def __init__(self, obj: Any, path: str) -> None:
        self.obj = obj
        if not self._validate_path(path):
            raise ValueError("Invalid path")
        self.path = path
        self.accessors = []
        self._build()

    def _validate_path(self, path) -> bool:
        if path == "":
            return True
        if self.PATH_VALIDATION_REGEX.match(path) is None:
            return False
        return True

    def _make_accessor(self, subscription: Union[str, int]) -> Callable:
        def func(obj):
            return operator.getitem(obj, subscription)

        return func

    def _build(self):
        """Build a list of attribute accessors from the given path.

        The `PARSE_REGEX.findall` returns a list of tuples, the tuples are either of
        shape ("string", "") or of ("", "int")."""

        groups = self.PARSE_REGEX.findall(self.path)
        accessors = []
        for group in groups:
            if group[0] == "":
                # of shape ("", "int")
                accessors.append(self._make_accessor(int(group[1])))
            elif group[1] == "":
                # of shape ("string", "")
                accessors.append(self._make_accessor(group[0]))
            else:
                raise Exception("Unexpected parse result")
        self.accessors = accessors

    def is_resolvable(self) -> bool:
        try:
            self.resolve()
            return True
        except UnresolvableError:
            return False

    def resolve(self) -> Any:
        """Return the value identified by the path"""
        current = self.obj
        for accessor in self.accessors:
            print(current)
            try:
                current = accessor(current)
            except (KeyError, TypeError, IndexError):
                raise UnresolvableError("Path is unresolvable on the object")
        return current
