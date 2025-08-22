from dataclasses import dataclass

from compy_python.ownership import mov, Valu


@dataclass
class FirstDataClass:
    field1: Valu(str)
    field2: int


@dataclass
class DataClassWithReference:
    field1: str  # pass-by-reference is the default
    field2: int


@dataclass
class _PrivateDataClass:
    field1: int


@dataclass(frozen=True)
class FrozenDataClass:
    field1: Valu(str)
    field2: int


@dataclass(frozen=True, slots=True)
class FrozenDataClassWithReference:
    field1: str
    field2: int


def dataclass_fn():
    print("DATACLASS RESULTS:")
    # basic
    a: FirstDataClass = FirstDataClass("the answer to the universe and everything:", 42)
    print(a.field1, a.field2)
    # with reference
    b: str = "abc"
    c: DataClassWithReference = DataClassWithReference(b, 1)
    print(c.field1, c.field2)
    # with mov
    d: str = "xyz"
    e: FirstDataClass = FirstDataClass(mov(d), 2)
    print(e.field1, e.field2)
    # frozen
    f: FrozenDataClass = FrozenDataClass("a", 3)
    print(f.field1, f.field2)
    # frozen with reference
    g: str = "abc"
    h: FrozenDataClassWithReference = FrozenDataClassWithReference(g, 4)
    print(h.field1, h.field2)
    # frozen with mov
    i: str = "xyz"
    j: FrozenDataClass = FrozenDataClass(mov(i), 5)
    print(j.field1, j.field2)
