def ranges_fn():
    print("RANGE RESULTS:")
    # single arg
    a: range = range(10)
    _iter_and_print(a)
    # 2 args
    _iter_and_print(range(10, 19))
    # 3 args
    _iter_and_print(_range_as_return())
    # show that if the range is used directory in the for loop then the traditional
    #  C++ for loop syntax is used.
    for i in range(10, 5, 1):
        print(i)
    print(range(10))
    print(range(5, 10))
    print(range(10, 5, -1))
    print(range(5, 10, 1))
    # TODO: test accessing the attributes


def _iter_and_print(arg1: range):
    a1: list[int] = []
    for i in arg1:
        a1.append(i)
    print(a1)


def _range_as_return() -> range:
    return range(9, 1, -2)
