from typing import Any, Generic, TypeVarTuple

Ts = TypeVarTuple("Ts")


class Uni(Generic[*Ts]):
    def __init__(self, value: Any):
        self._value = value


T = TypeError("T")


def isinst(obj: Uni[*Ts], _type: type[T]) -> bool:
    return isinstance(obj._value, _type)


def vg(obj: Uni[*Ts], _type: type[T]) -> Any:
    return obj._value
