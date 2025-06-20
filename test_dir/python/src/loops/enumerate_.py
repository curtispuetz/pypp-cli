from test_dir.python.pypp.tuple_get import pypp_tg


def enumerate_fn():
    # over a list
    a: list[int] = []
    for i, val in enumerate([1, 2, 3]):
        a.append(i)
        a.append(val)
    print(a)
    # Note: a second argument to enumerate is not supported and will result in a C++
    # compilation error.
    # for i, val in enumerate([1, 2, 3], 7):
    # over a set
    for i, val in enumerate({-1, -3}):
        a.append(i)
        a.append(val)
    print(a)
    # over a dicts keys
    d: dict[int, int] = {0: 1, 1: 2}
    for i, val in enumerate(d.keys()):
        a.append(i)
        a.append(val)
    print(a)
    # over a dicts values
    for i, val in enumerate(d.values()):
        a.append(i)
        a.append(val)
    print(a)
    # over a dicts items
    for i, val in enumerate(d.items()):
        a.append(i)
        a.append(pypp_tg(val, 0))
        a.append(pypp_tg(val, 1))
    print(a)
