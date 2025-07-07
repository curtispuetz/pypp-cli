from dataclasses import dataclass

from test_dir.python.pypp.ownership import Ref, mov


@dataclass
class FirstDataClass:
    field1: str
    field2: int

@dataclass
class DataClassWithReference:
    field1: Ref(str)
    field2: int

def dataclass_fn():
    # basic
    a: FirstDataClass = FirstDataClass("the answer to the universe and everything", 42)
    print(f"field1: {a.field1}, field2: {a.field2}")
    # with reference
    b: str = "abc"
    c: DataClassWithReference = DataClassWithReference(b, 1)
    print(f"field1: {c.field1}, field2: {c.field2}")
    # with mov
    d: str = "xyz"
    e: FirstDataClass = FirstDataClass(mov(d), 2)
    print(f"field1: {e.field1}, field2: {e.field2}")
