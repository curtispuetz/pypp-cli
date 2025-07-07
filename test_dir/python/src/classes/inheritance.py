class BaseClass:
    def __init__(self, a: int):
        self.a = a

    def add(self, val: int) -> int:
        return self.a + val

    def add2(self, val: int) -> int:
        return self.a + val


class BaseClass2:
    def __init__(self, z: int):
        self.z = z

    def mult2(self, val: int) -> int:
        return 2 * self.z * val


class ChildClass(BaseClass):
    def __init__(self, a: int, b: int):
        BaseClass.__init__(self, a)
        self.b = b

    def add(self, val: int) -> int:
        return self.add2(val)

    def multiply(self, val: int) -> int:
        return self.a * self.b * val


class ChildClass2(ChildClass):
    def __init__(self, a: int, b: int, c: int):
        ChildClass.__init__(self, a, b)
        self.c = c

    def add(self, val: int) -> int:
        return self.add2(val)


class ChildMultiple(BaseClass, BaseClass2):
    def __init__(self, a: int, b: int, c: int):
        BaseClass.__init__(self, a)
        BaseClass2.__init__(self, b)
        self.c = c

    def add(self, val: int) -> int:
        return self.a + self.z + val


def class_inheritance_fn():
    print("CLASS INHERITANCE RESULTS:")
    # basic
    a: ChildClass = ChildClass(2, 2)
    print(a.add(3))
    print(a.multiply(3))
    b: ChildClass2 = ChildClass2(3, 3, 3)
    print(b.add(4))
    # multiple inheritance
    c: ChildMultiple = ChildMultiple(4, 4, 4)
    print(c.add(5))
    print(c.mult2(5))
