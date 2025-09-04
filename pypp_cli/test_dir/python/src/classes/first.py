from pypp_python import Valu, mov


class ClassA:
    def __init__(self, a: int, b: str):
        self.a = a
        self.b = b

    def add(self, c: int) -> int:
        return self.a + c


class ClassWithPassByValue:
    def __init__(self, a: int, b: Valu(str)):
        self.a = a
        self.b = b


class _PrivateClass:
    def __init__(self, a: int):
        self.a = a


def classes_fn():
    print("CLASSES RESULTS:")
    # basic
    a: str = "hello"
    b: ClassA = ClassA(1, a)
    print(b.add(2))
    print(b.b)
    # pass by value
    c: ClassWithPassByValue = ClassWithPassByValue(1, "world")
    print(c.b)
    # mov
    d: str = "abc"
    e: ClassWithPassByValue = ClassWithPassByValue(1, mov(d))
    print(e.b)
    # private
    f: _PrivateClass = _PrivateClass(3)
    print(f.a)
