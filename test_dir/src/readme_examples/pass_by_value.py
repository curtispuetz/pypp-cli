from pypp_python import Valu


def pass_by_value_fn(a: Valu(list[int]), _b: Valu(list[int])) -> list[int]:
    return a
