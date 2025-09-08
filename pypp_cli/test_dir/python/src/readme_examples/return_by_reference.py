from pypp_python import Ref


def return_by_reference_fn(a: list[int], b: list[int]) -> Ref(list[int]):
    return a
