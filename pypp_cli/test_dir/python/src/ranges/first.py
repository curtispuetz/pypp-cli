from pypp_python import mov


def _iter_and_print(arg1: range):
    a1: list[int] = []
    for i in arg1:
        y: int = i
        a1.append(mov(y))
    print(a1)


def _range_as_return() -> range:
    return range(9, 1, -2)


def ranges_fn():
    print("RANGE RESULTS:")
    # single arg
    a: range = range(10)
    _iter_and_print(a)
    # example 2
    a0: range = _range_as_return()
    _iter_and_print(a0)
    # show that if the range is used directory in the for loop then the traditional
    #  C++ for loop syntax is used.
    for i in range(10, 5, 1):
        print(i)
    print(range(10))
    print(range(5, 10))
    print(range(10, 5, -1))
    print(range(5, 10, 1))
    # using as a key
    b: dict[range, int] = {a: 1, range(1, 4): 2}
    print(b)
