from test_dir.python.pypp.dict_get import pypp_dg_opt, pypp_dg
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
    b: PyppOpt[str] = pypp_dg_opt(a, 1)
    if b.has_value():
        print(b.value())
    c: PyppOpt[str] = pypp_dg_opt(a, -1)
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
    # note: items() should only be used for iterating over in a loop for now.
    # print(a.items())
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
    _fn_dict_arg({0: 1, 1: 2})
    # TODO later: handle addition
    # print({0: 1} | {1: 2})
    # initialize empty
    e: dict[int, int] = {}
    print(e)
    # a nested dict
    f: dict[int, dict[int, int]] = {0: {0: 1}, 1: {0: 1}}
    print(f)
    # TODO: test exceptions for all types (tuple, string, set, list, dict, np_arr, numbers)
    # modifying references
    f0: dict[int, int] = f[0]
    f0[99] = 98
    print(f)
    f[1][77] = 76
    print(f)
    f1: PyppOpt[dict[int, int]] = pypp_dg_opt(f, 1)
    if f1.has_value():
        f1.value()[9] = 8
    print(f)
    # test pypp_dg
    g: dict[int, int] = {0: 1, 1: 2}
    g0: int = pypp_dg(g, 1)
    print(str(g0))


def _fn_dict_arg(d: dict[int, int]):
    print(d)
