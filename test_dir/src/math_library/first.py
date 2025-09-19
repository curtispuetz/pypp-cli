from pypp_python.stl import math


def math_library_fn():
    print("MATH LIBRARY RESULTS:")
    # Assign results to variables
    sqrt_result: float = math.sqrt(9)
    hypot_result: float = math.hypot(3, 4)
    floor_result: int = math.floor(3.5)
    ceil_result: int = math.ceil(3.5)
    pi_value: float = math.pi
    sin_result: float = math.sin(math.pi / 2)
    cos_result: float = math.cos(math.pi / 4)
    tan_result: float = math.tan(math.pi / 4)
    radians_result: float = math.radians(90)
    print(sqrt_result)
    print(hypot_result)
    print(floor_result)
    print(ceil_result)
    print(pi_value)
    print(sin_result)
    print(cos_result)
    print(tan_result)
    print(radians_result)
    # Note: other math functions will also work if their name in python (math.name)
    #  matches identically to their name in C++ from the cmath library (std::name). If,
    #  they are not supported yet.
