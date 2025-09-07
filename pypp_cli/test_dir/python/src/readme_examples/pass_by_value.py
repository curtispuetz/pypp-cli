from pypp_python import Valu, Ref


def my_function(a: Valu(list[int]), b: Valu(list[int])) -> Ref(list[int]):
    ret: list[int] = [1, 2, 3]
    assert len(a) == len(b), "List lengths should be equal"
    for i in range(len(a)):
        ret.append(a[i] + b[i])
    return ret
