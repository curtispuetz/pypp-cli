from pypp_python import mov


def zip_fn():
    print("ZIP RESULTS:")
    # over two lists
    a: list[int] = []
    for x, z in zip([1, 2], [3, 4]):
        xx: int = x
        zz: int = z
        a.append(mov(xx))
        a.append(mov(zz))
    print(a)
    # over multiple different types. list, set, string, and dict items
    for x, z, y in zip([1, 2], {"a", "b"}, "ab"):
        # Note: The sets in C++ order is not guaranteed, so you could see
        # different strings
        print(f"{x}, {z}, {y}")
