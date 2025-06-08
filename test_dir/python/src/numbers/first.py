def number_ops():
    a: int = 1 + 2
    print(str(a))
    print(str(2 + 2))
    print(str(2 * 2))
    print(str(4 / 2))
    b: float = 4 + 10 - 5 * 5.0 / 2
    print(str(b))
    c: int = (5 + 10) * (2 + 2) * (5 + 4 + 10)
    print(str(c))
    # NOTE: the bedmass operators seem to work. The C++ gets some extra brackets, but it
    # is fine.
    d: int = ((10 * 40) + (4 + 2 * 4 + 4)) * (10 * 2)
    e: int = 4 + 2 * 4 + 4
    print(str(d))
    print(str(e))
