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
    f: int = 10 // 5
    print(str(f))
    print(str(-7 // 2))  # Should be -4
    g: int = (-14 // 2) // ((-2 + 4) * 1)  # Should be -4
    print(str(g))
    # aug assignments
    g += 2
    print(str(g))
    g -= 2
    print(str(g))
    g *= 5
    print(str(g))
    g /= 5
    print(str(g))
