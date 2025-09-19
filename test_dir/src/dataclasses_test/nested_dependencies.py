from pypp_python import dataclass


@dataclass
class _ClassA:
    a: int


@dataclass
class _ClassB:
    b: int
    class_a: _ClassA


@dataclass
class _ClassC:
    c: int
    class_b: _ClassB

    def access(self) -> int:
        return self.class_b.class_a.a


def dataclass_nested_dependencies_fn():
    print("DATACLASS NESTED DEPENDENCIES RESULTS:")
    class_a: _ClassA = _ClassA(1)
    class_b: _ClassB = _ClassB(2, class_a)
    class_c: _ClassC = _ClassC(3, class_b)
    print(class_c.access())
