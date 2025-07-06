from typing import TypeVar, Annotated

T = TypeVar("T")


def mov(obj: T) -> T:
    return obj

class PassByValue:
    """
    A marker class to indicate that an object is passed by value.
    pass-by-reference is the default.
    """

def Valu(typ: T) -> Annotated[T, PassByValue()]:
    return Annotated[typ, PassByValue()]
