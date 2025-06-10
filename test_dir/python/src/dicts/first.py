from test_dir.python.pypp.optional import PyppOpt


def dict_fn():
    # declaration
    a: dict[int, str] = {0: "a", 1: "b", 2: "c"}
    print(a)
    # access
    print(a[0])
    # get
    default_v: str = a.get(-1, "default value")
    print(default_v)
    b: PyppOpt[str] = PyppOpt(a.get(1))
    if b.has_value():
        print(b.value())
    c: PyppOpt[str] = PyppOpt(a.get(-1))
    if not c.has_value():
        print("no value")
    print(c.value_or("no value from value_or"))
    # setting
    a[3] = "d"
    print(a)
    val: str = a.setdefault(4, "e")
    print(val)
    print(a)
    val = a.setdefault(4, "f")
    print(val)
    print(a)
    # keys
    print(a.keys())
    # values
    print(a.values())
    # items
    print(a.items())
