from pypp_python import dataclass


@dataclass
class DataClassWithMethods:
    field1: int

    def add(self, x: int) -> int:
        return self.field1 + x

    def subtract(self, x: int) -> int:
        return self.field1 - x


@dataclass
class _PrivateDataClassWithMethods:
    field1: int

    def add(self, x: int) -> int:
        return self.field1 + x


def dataclass_with_methods_fn():
    print("DATACLASS WITH METHODS RESULTS:")
    # method signatures in .h file, implementations in .cpp file
    k: DataClassWithMethods = DataClassWithMethods(2)
    print(k.add(1), k.subtract(1))
    # private dataclass
    p: _PrivateDataClassWithMethods = _PrivateDataClassWithMethods(3)
    print(p.add(2))
