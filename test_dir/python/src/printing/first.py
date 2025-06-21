# TODO: consider fixing the inconsistent quotes around strings printed from the C++
#  side. It is inconsistent with the Python printing
def printing_fn():
    print("PRINTING RESULTS:")
    # integer
    print(1)
    # float
    print(1.2)
    # boolean
    print(True)
    # list
    print([1, 2, 3])
    # set
    print({1, 2, 3})
    # dict
    a: dict[int, int] = {0: 1, 1: 2}
    print(a)
    # nested list
    print([[[-1]]])
    # tuple
    print((1, 2))
    # multiple arguments
    print(1, 2, 3, 4)
    print(
        "multiple arguments:",
        [1, 2],
        a,
        {1, 2},
        (5, 6),
        3.14,
        a.keys(),
        a.values(),
        a.items(),
    )
