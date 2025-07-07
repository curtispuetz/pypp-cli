class BaseClass:
    def __init__(self, a: int):
        self.a = a

    def add(self, val: int) -> int:
        return self.a + val

    def add2(self, val: int) -> int:
        return self.a + val


class ChildClass(BaseClass):
    def __init__(self, a: int, b: int):
        BaseClass.__init__(self, a)
        self.b = b

    def add(self, val: int) -> int:
        return self.add2(val)

    def multiply(self, val: int) -> int:
        return self.a * self.b * val


def class_inheritance_fn():
    print("CLASS INHERITANCE RESULTS:")
    # basic
    a: ChildClass = ChildClass(2, 2)
    print(a.add(3))
    print(a.multiply(3))
