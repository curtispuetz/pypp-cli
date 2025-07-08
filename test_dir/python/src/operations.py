from test_dir.python.pypp.math import int_pow


def operations_fn():
    print("OPERATIONS RESULTS:")
    # float power
    a: float = 2**3
    print(f"float power: {a}")
    # int power. Note: for safety, you need to use for integer exponentiation because
    #  C++ does not have safe integer exponentiation.
    b: int = int_pow(2, 3)
    print(f"int power: {b}")
