from test_dir.python.pypp.tuple_get import pypp_tg

# TODO: make sure that when you pass values to a tuple it automatically moves the values
#  it should work by this by default and this should be the only way tuples are used.
# TODO: in general specify the tuple design. The thing above is one part of it, and
#  another is when you do a, b = my_tup you get references. Another I think is when you
#  do a, b = my_fn_that_returns_tup() you get the actual values.

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
    # inline passing
    _inline_tuple((1.2, "z"))
    # unpacking elements
    x, y, z = a
    print(x, y, z)
    # unpacking elements from a function
    u, v = get_tup()
    print(u, v)


def _inline_tuple(tup: tuple[float, str]):
    print(tup)

def get_tup() -> tuple[int, float]:
    return 1, 2.0