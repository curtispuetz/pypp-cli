class _PrivateClass:
    def __init__(self, abc: int):
        self.xyz = abc


class ClassA:
    def __init__(self, x: int, y: int, z: int):
        self._x = x
        self._y = y
        self._z = z


class ClassWithDifferentOrder:
    # shows that the order of assignments does not matter
    def __init__(self, x: int, y: int, z: int):
        self._z = z
        self._x = x
        self._y = y
