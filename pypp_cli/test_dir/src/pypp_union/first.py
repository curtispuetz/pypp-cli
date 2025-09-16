from dataclasses import dataclass
from pypp_python import Uni, ug, isinst, is_none, Valu, mov, Ref, auto


@dataclass
class ClassWithUnion:
    value: Uni[int, float]

    def calc(self) -> int:
        if isinst(self.value, int):
            return ug(self.value, int) * 2
        return 0


@dataclass
class ClassWithUnionByValue:
    value: Valu(Uni[int, float])


def pypp_union_fn():
    print("pypp UNION RESULTS:")
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
    print(Ref(f))
    # inline
    g: ClassWithUnionByValue = ClassWithUnionByValue(Uni[int, float](7))
    print(Ref(g))
    # with auto
    h: auto = Uni[int, float](2.71)
    print(h)
    # equality operators
    print(a == Uni[int, float](3.14))
    print(a != Uni[int, float](3.14))
