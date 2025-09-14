def dict_looping_fn():
    print("DICT LOOPING RESULTS:")
    # over a dict's items
    d: dict[int, int] = {0: 1, 1: 2, 2: 3}
    for i, k in enumerate(d.keys()):
        print(f"{i}: {k} -> {d[k]}")
    for i, k, v in zip([1, 2, 3], d.keys(), d.values()):
        print(f"{i}: {k} -> {v}")
