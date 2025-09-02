from compy_python import tg, mov


def enumerate_fn():
    print("ENUMERATE RESULTS:")
    # over a list
    a: list[int] = []
    for i, val in enumerate([1, 2, 3]):
        # Note: you don't need to use mov with the enumerate counter.
        a.append(i)
        a.append(mov(val))
    print(a)
    # Note: a second argument to enumerate is not supported and will result in a C++
    # compilation error.
    # for i, val in enumerate([1, 2, 3], 7):
    # over a set
    for i, val in enumerate({-1, -3}):
        a.append(i)
    print(a)
    # over a dicts keys
    d: dict[int, int] = {0: 1, 1: 2}
    for i, val in enumerate(d.keys()):
        a.append(i)
    print(a)
    # over a dicts values
    for i, val in enumerate(d.values()):
        a.append(i)
    print(a)
    # over a dicts items
    for i, val in enumerate(d.items()):
        a.append(i)
        # Note: Of course I can't move this directly to the 'a' list without making a
        #  copy first because the data is owned by the dict.
        y: int = tg(val, 0)
        a.append(mov(y))
    print(a)
