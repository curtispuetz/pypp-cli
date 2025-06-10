from typing import Annotated, TypeVar

T = TypeVar("T")


class Mutated:
    """Marker metadata indicating in-place mutation."""


# PyppMut is the way in Py++ that you specify a function/method arg as mutatable.
# You cannot mutate a function/method arg and have a working C++ build without using
# PyppMut. The internal reason for this that the arguments in the C++ code are always a
# constant reference, unless the PyppMut annotation is used, in which case the constant
# part is removed.


def PyppMut(typ: T) -> Annotated[T, Mutated()]:
    return Annotated[typ, Mutated()]
