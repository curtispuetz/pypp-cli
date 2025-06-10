from typing import Generic, TypeVar, Optional

# PyppOpt is the Py++ way of handling optional values, since you cannot use the None
# keyword in Py++ and have a working C++ build.

# Important note to Py++ users is that any Python function or method you call that can
# return None, you must wrap it with PyppOpt. For example, the dictionary get method.
# Instead of:
# 'a: str | None = my_dict.get(1)'
# should do:
# 'a: PyppOpt = PyppOpt(my_dict.get(1))'

# Note about conversion of this to C++ code
# Whenever PyppOpt is used with no args the C++ code is std::nullopt, and whenever it
# is used with the single argument the C++ code is that single argument.

T = TypeVar("T")


class PyppOpt(Generic[T]):
    __slots__ = ("_value", "_has_value")

    def __init__(self, value: Optional[T] = None):
        if value is not None:
            self._value: T = value
            self._has_value: bool = True
        else:
            self._value = None  # type: ignore
            self._has_value = False

    def has_value(self) -> bool:
        return self._has_value

    def value(self) -> T:
        if not self._has_value:
            raise ValueError("Optional has no value")
        return self._value

    def value_or(self, default: T) -> T:
        return self._value if self._has_value else default

    def reset(self):
        self._value = None
        self._has_value = False

    def emplace(self, value: T):
        self._value = value
        self._has_value = True

    def __bool__(self) -> bool:
        return self._has_value

    def __eq__(self, other: object) -> bool:
        if isinstance(other, PyppOpt):
            return self._has_value == other._has_value and self._value == other._value
        if other is None:
            return not self._has_value
        return False

    def __ne__(self, other: object) -> bool:
        return not self.__eq__(other)

    def __repr__(self) -> str:
        if self._has_value:
            return f"Optional({self._value!r})"
        return "Optional(None)"


def a(b: int) -> PyppOpt[int]:
    if b > 0:
        return PyppOpt(1)
    return PyppOpt()
