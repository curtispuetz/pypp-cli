from typing import Callable

from pypp_python import configclass

a: int = 2
b: str = "b"

A: int = 1
B: str = "B"
C: list[int] = [1, 2, 3]
D: dict[int, int] = {0: 1}
E: set[int] = {1, 2, 3}

# private
_A: int = 2

# A function
G: Callable[[int], int] = lambda x: x + 1


@configclass
class MyConfig:
    a: int = 1
    b: str = "2"


@configclass(dtype=str)
class MyConfig2:
    a = "a"
    b = "b"


@configclass(dtype=int)
class _PrivateConfig:
    a = 1
    b = 2


# inside function
def constant_fn():
    print("CONSTANT RESULTS:")
    # Show the nuance of how if you define a constant at a non-module level and
    # without starting with an underscore, the constant is actually extracted to the
    # header file in the transpiled C++. If the name starts with an underscore this is
    # not the case.
    F: int = 3
    _F: int = 4
    print(F)
    print(_F)
    print(G(1))  # should print 2
    # config classes
    print(MyConfig.a, MyConfig.b)
    print(MyConfig2.a, MyConfig2.b)
    print(_PrivateConfig.a, _PrivateConfig.b)
