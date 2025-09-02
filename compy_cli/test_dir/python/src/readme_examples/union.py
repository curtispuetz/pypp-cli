from compy_python import Uni, ug, isinst, is_none


def union_example():
    int_float_or_list: Uni[int, float, list[int]] = Uni(3.14)
    if isinst(int_float_or_list, float):
        val: float = ug(int_float_or_list, float)
        print(val)
    # Union with None
    b: Uni[int, None] = Uni(None)
    if is_none(b):
        print("b is None")
