def for_loop_fn():
    # looping with 'range()'
    ret: list[int] = []
    for i in range(2, 10, 2):
        ret.append(i)
    print(ret)
    # looping over a list
    a: list[int] = []
    for val in ret:
        a.append(val)
    print(a)
    # looping over a set
    b: set[int] = {10, 20, 30}
    for val in b:
        a.append(val)
    print(a)
    # looping over a dict keys
    c: dict[int, int] = {0: 1, 1: 2}
    for k in c.keys():
        a.append(k)
    print(a)
    # looping over a dict values
    for v in c.values():
        a.append(v)
    print(a)
    # looping over a dict items
    for k, v in c.items():
        a.append(k)
        a.append(v)
    print(a)
    # looping over list of tuples
    d: list[tuple[int, int]] = [(1, 2), (3, 4)]
    for first, second in d:
        a.append(first)
        a.append(second)
    print(a)
    print(d)
    # looping over nested dicts
    e: dict[int, dict[int, dict[int, int]]] = {0: {0: {0: 1, 2: 3}}}
    for k1, v1 in e.items():
        for k2, v2 in v1.items():
            for k3, v3 in v2.items():
                a.append(k3)
                a.append(v3)
    print(a)
