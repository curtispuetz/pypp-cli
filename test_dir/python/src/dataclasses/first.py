from dataclasses import dataclass


@dataclass
class FirstDataClass:
    field1: str
    field2: int


def dataclass_fn():
    a: FirstDataClass = FirstDataClass("the answer to the universe and everything", 42)
    print(f"field1: {a.field1}, field2: {a.field2}")
