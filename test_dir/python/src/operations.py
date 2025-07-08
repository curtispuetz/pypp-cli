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
    # mod
    c: int = 10 % 3
    print(f"mod: {c}")
    # left shift
    d: int = 1 << 2
    print(f"left shift: {d}")
    # right shift
    e: int = 4 >> 1
    print(f"right shift: {e}")
    # bitwise or
    f: int = 1 | 2
    print(f"bitwise or: {f}")
    # bitwise xor
    g: int = 1 ^ 2
    print(f"bitwise xor: {g}")
    # bitwise and
    h: int = 1 & 2
    print(f"bitwise and: {h}")
    # not
    i: bool = not True
    print(f"not: {i}")
    # usub
    j: int = -5
    print(f"usub: {j}")
    # uadd
    k: int = +5
    print(f"uadd: {k}")
    # invert
    l: int = ~5
    print(f"invert: {l}")
