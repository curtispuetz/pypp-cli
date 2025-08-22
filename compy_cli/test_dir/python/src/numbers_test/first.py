def number_ops():
    print("NUMBER RESULTS:")
    a: int = 1 + 2
    print(a)
    print(2 + 2)
    print(2 * 2)
    print(4 / 2)
    b: float = 4 + 10 - 5 * 5.0 / 2
    print(b)
    c: int = (5 + 10) * (2 + 2) * (5 + 4 + 10)
    print(c)
    # NOTE: the bedmass operators seem to work. The C++ gets some extra brackets, but it
    # is fine.
    d: int = ((10 * 40) + (4 + 2 * 4 + 4)) * (10 * 2)
    e: int = 4 + 2 * 4 + 4
    print(d)
    print(e)
    f: int = 10 // 5
    print(f)
    print(-7 // 2)  # Should be -4
    g: int = (-14 // 2) // ((-2 + 4) * 1)  # Should be -4
    print(g)
    # aug assignments
    h: float = -4.1
    h += 2
    print(h)
    h -= 2
    print(h)
    h *= 5
    print(h)
    h /= 5
    print(h)
