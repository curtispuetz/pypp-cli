from typing import Callable

A: int = 1
B: str = "B"
C: list[int] = [1, 2, 3]
D: dict[int, int] = {0: 1}
E: set[int] = {1, 2, 3}

# private
_A: int = 2

# A function
G: Callable[[int], int] = lambda x: x + 1


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
