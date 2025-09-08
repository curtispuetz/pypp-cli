def built_in_dict_fn():
    print("BUILT-IN DICT FUNCTION RESULTS:")
    a: dict[str, int] = {"one": 1, "two": 2, "three": 3}
    b: dict[str, int] = dict(a)
    a["four"] = 4
    print(a)
    print(b)
    c: dict[str, int] = dict([("one", 1), ("two", 2), ("three", 3)])
    print(c)
    d: dict[float, str] = dict[float, str]()
    print(d)
