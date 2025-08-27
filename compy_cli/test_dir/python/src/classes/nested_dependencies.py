class _ClassA:
    def __init__(self, a: int) -> None:
        self.a = a


class _ClassB:
    def __init__(self, b: int, class_a: _ClassA) -> None:
        self.b = b
        self.class_a = class_a


class _ClassC:
    def __init__(self, c: int, class_b: _ClassB) -> None:
        self.c = c
        self.class_b = class_b

    def access(self) -> int:
        return self.class_b.class_a.a


def class_nested_dependencies_fn():
    print("CLASS NESTED DEPENDENCIES RESULTS:")
    class_a: _ClassA = _ClassA(1)
    class_b: _ClassB = _ClassB(2, class_a)
    class_c: _ClassC = _ClassC(3, class_b)
    print(class_c.access())
