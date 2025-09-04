from pypp_python import int_pow, Ref


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
    l1: int = ~5
    print(f"invert: {l1}")
    # is
    t1: list[int] = [1, 2]
    t2: Ref(list[int]) = t1
    m: bool = t1 is t2
    print(f"is: {m}")
    # is not
    n: bool = t1 is not t2
    print(f"is not: {n}")
    # in list
    o: bool = 5 in [1, 5]
    print(f"in: {o}")
    # in set
    p: bool = 5 in {1, 5}
    print(f"in set: {p}")
    # in dict
    # Note: I create a test_dict because you can't inline the dicts like the others in
    # Py++. Is this still true or is that possible now?
    test_dict: dict[int, str] = {1: "a", 5: "b"}
    q: bool = 5 in test_dict
    print(f"in dict: {q}")
    # in tuple
    r: bool = 5 in (1, 5)
    print(f"in tuple: {r}")
    # in string
    s: bool = "abc" in "zzabczz"
    print(f"in string: {s}")
    # not in list
    t: bool = 5 not in [1, 2]
    print(f"not in: {t}")
    # not in set
    u: bool = 5 not in {1, 2}
    print(f"not in set: {u}")
    # not in dict
    v: bool = 5 not in test_dict
    print(f"not in dict: {v}")
    # not in tuple
    w: bool = 5 not in (1, 2)
    print(f"not in tuple: {w}")
    # not in string
    x: bool = "abc" not in "zzxyz"
    print(f"not in string: {x}")
    print("printing reference:")
    print(Ref(x))
