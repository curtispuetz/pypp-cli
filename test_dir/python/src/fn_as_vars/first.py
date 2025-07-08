from typing import Callable


def _test_fn(a: int, b: int) -> str:
    return f"{a} {b}"


def fn_as_vars_fn():
    print("FN_AS_VARS RESULTS:")
    # assign function to variable
    fn_var: Callable[[int, int], str] = _test_fn
    print(fn_var(1, 2))
