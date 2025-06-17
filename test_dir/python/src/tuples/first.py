from test_dir.python.pypp.tuple_get import pypp_tg


def tuples_fn():
    print("TUPLE RESULTS:")
    a: tuple[int, float, str] = (1, 1.2, "a")
    # count
    print(str(a.count(2)))
    # index
    print(str(a.index(1.2)))
    # print(a.index(1.1))  # Throws error
    # access
    b: int = pypp_tg(a, 0)
    print(str(b))
    # comparisons
    print(str((1, 2) == (1, 2)))
    print(str((1, 2) != (1, 2)))
    print(str((1, 2) < (1, 2)))
    print(str((1, 2) <= (1, 2)))
    print(str((1, 2) > (1, 2)))
    print(str((1, 2) >= (1, 2)))
    # printing
    print((1, 2))
    print((1, 2, "a"))
    # length
    print(str(len((1, 2))))
