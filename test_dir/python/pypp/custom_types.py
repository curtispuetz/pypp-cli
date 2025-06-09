from typing import Annotated, TypeVar

T = TypeVar("T")


class Mutated:
    """Marker metadata indicating in-place mutation."""


def PyppMut(typ: T) -> Annotated[T, Mutated()]:
    return Annotated[typ, Mutated()]
