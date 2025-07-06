from test_dir.python.pypp.ownership import Ref


def ref_vars_fn():
    print("REF VARS RESULTS:")
    a: list[list[int]] = [[1, 2], [3, 4]]
    print(a)
    # copy
    b: list[int] = a[0]
    b.append(5)
    print("Python and C++ should print different results:")
    print(a)
    # reference
    c: list[list[int]] = [[1, 2], [3, 4]]
    d: Ref(list[int]) = c[0]
    d.append(5)
    print("Python and C++ should print the same results:")
    print(c)
    # with dicts
    e: dict[int, list[int]] = {0: [1, 2], 1: [3, 4]}
    f: Ref(list[int]) = e[0]
    f.append(5)
    print("Python and C++ should print the same results:")
    print(e)