from compy_python.ownership import Valu, mov
from compy_python.printing import print_address
from compy_python.union import Uni, ug, isinst, is_none


class ClassWithUnion:
    def __init__(self, value: Uni[int, float]):
        self.value = value

    def calc(self) -> int:
        if isinst(self.value, int):
            return ug(self.value, int) * 2
        return 0


class ClassWithUnionByValue:
    def __init__(self, value: Valu(Uni[int, float])):
        self.value = value


def pypp_union_fn():
    print("PYPP UNION RESULTS:")
    a: Uni[int, float] = Uni(3.14)
    if isinst(a, float):
        print(ug(a, float))
    if not isinst(a, int):
        print("a is not an int")
    # Union with None
    b: Uni[int, None] = Uni(None)
    if is_none(b):
        print("b is None")
    # passing union to object
    c: Uni[int, float] = Uni(42)
    d: ClassWithUnion = ClassWithUnion(c)
    print(d.calc())
    # passing union with mov
    e: Uni[int, float] = Uni(3.14)
    f: ClassWithUnionByValue = ClassWithUnionByValue(mov(e))
    print_address(f)
