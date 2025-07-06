from typing import TypeVar, Annotated

T = TypeVar("T")


def mov(obj: T) -> T:
    return obj

class PassByValue:
    pass

def Valu(typ: T) -> Annotated[T, PassByValue()]:
    return Annotated[typ, PassByValue()]

class TypeIsARef:
    pass

def Ref(typ: T) -> Annotated[T, TypeIsARef()]:
    return Annotated[typ, TypeIsARef()]
