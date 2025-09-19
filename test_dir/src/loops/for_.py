from pypp_python import mov


def for_loop_fn():
    print("FOR RESULTS:")
    # looping with 'range()'
    ret: list[int] = []
    # 3 args
    for i in range(2, 10, 2):
        ret.append(mov(i))
    # 2 args
    for j in range(2, 4):
        ret.append(mov(j))
    # 1 arg
    for k in range(2):
        ret.append(mov(k))
    print(ret)
    # looping over a list
    a: list[int] = []
    for val in ret:
        y: int = val
        a.append(mov(y))
    print(a)
    # looping over a set
    b: set[int] = {10, 20, 30}
    for val in b:
        y: int = val
        a.append(mov(y))
    print(a)
    # looping over a dict keys
    c: dict[int, int] = {0: 1, 1: 2}
    for k in c.keys():
        y: int = k
        a.append(mov(y))
    print(a)
    # looping over a dict values
    for v in c.values():
        y: int = v
        a.append(mov(y))
    print(a)
    # looping over a dict items
    for k, v in c.items():
        x: int = k
        y: int = v
        a.append(mov(x))
        a.append(mov(y))
    print(a)
    # looping over list of tuples
    d: list[tuple[int, int]] = [(1, 2), (3, 4)]
    for first, second in d:
        x: int = first
        y: int = second
        a.append(mov(x))
        a.append(mov(y))
    print(a)
    print(d)
    # looping over nested dicts
    e: dict[int, dict[int, dict[int, int]]] = {0: {0: {0: 1, 2: 3}}}
    for k1, v1 in e.items():
        for k2, v2 in v1.items():
            for k3, v3 in v2.items():
                x: int = k3
                y: int = v3
                a.append(mov(x))
                a.append(mov(y))
    print(a)
