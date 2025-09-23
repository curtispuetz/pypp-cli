from pypp_python import Val


def pass_by_value_fn(a: Val[list[int]], _b: Val[list[int]]) -> list[int]:
    return a
