from dataclasses import dataclass

from test_dir.python.pypp.ownership import Ref


@dataclass
class FirstDataClass:
    field1: str
    field2: int

@dataclass
class DataClassWithReference:
    field1: Ref(str)
    field2: int

def dataclass_fn():
    a: FirstDataClass = FirstDataClass("the answer to the universe and everything", 42)
    print(f"field1: {a.field1}, field2: {a.field2}")
    b: str = "abc"
    c: DataClassWithReference = DataClassWithReference(b, 1)
    print(f"field1: {c.field1}, field2: {c.field2}")
