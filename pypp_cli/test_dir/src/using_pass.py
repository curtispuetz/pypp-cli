from pypp_python import auto, Valu
from dataclasses import dataclass


def fn_that_uses_pass():
    pass


@dataclass
class ClassWithMethodThatUsesPass:
    my_list: Valu(list[int])

    def method(self):
        pass


def fn_with_if_that_uses_pass(x: int):
    if x > 0:
        pass
    else:
        print("x is not greater than 0")


def fn_with_loop_that_uses_pass():
    for i in range(10):
        pass


def fn_with_try_except_finally_that_uses_pass():
    try:
        raise ValueError("An error occurred")
    except ValueError:
        pass


def pass_fn():
    print("PASS RESULTS:")
    fn_that_uses_pass()
    obj2: auto = ClassWithMethodThatUsesPass([1, 2, 3])
    obj2.method()

    fn_with_if_that_uses_pass(5)
    fn_with_loop_that_uses_pass()
    fn_with_try_except_finally_that_uses_pass()
