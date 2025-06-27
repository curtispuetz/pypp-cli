import math


def math_library_fn():
    # TODO: test that you can assign each of these to variables.
    print("MATH LIBRARY RESULTS:")
    print(math.sqrt(9))
    print(math.hypot(3, 4))
    print(math.floor(3.5))
    print(math.ceil(3.5))
    print(math.pi)
    print(math.sin(math.pi / 2))
    print(math.cos(math.pi / 4))
    print(math.tan(math.pi / 4))
    a: float = math.radians(90)
    print(a)
    # Note: other math functions will also work if their name in python (math.name)
    #  matches identically to their name in C++ from the cmath library (std::name). If,
    #  they are not supported yet.
