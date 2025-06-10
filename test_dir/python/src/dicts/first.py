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
    # dict with list as value
    d: dict[int, list[int]] = {
        0: [1, 2, 3],
        1: [4, 5, 6],
    }
    print(d)
    # clear
    d.clear()
    d[0] = [1]
    print(d)
    # update
    a.update({4: "z", 5: "x"})
    print(a)
    # pop
    pop_val: str = a.pop(1)
    print(pop_val)
    print(a)
    pop_val = a.pop(10, "default value")
    print(pop_val)
    print(a)
    # length
    print(str(len(a)))
    # contains
    print(str(5 in a))
    # copy
    a_copy: dict[int, str] = a.copy()
    a.pop(0)
    print(a_copy)
    print(a)
