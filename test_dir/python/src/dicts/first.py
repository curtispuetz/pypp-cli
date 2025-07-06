from test_dir.python.pypp.dict_get import dg
from test_dir.python.pypp.ownership import mov, Valu


def _inline_dict(d: Valu(dict[int, int])):
    print(d)


def dict_fn():
    print("DICT RESULTS:")
    # declaration
    a: dict[int, str] = {0: "a", 1: "b", 2: "c"}
    print(a)
    # dg (better than access with [] because it throws)
    g: dict[int, int] = {0: 1, 1: 2}
    g0: int = dg(g, 1)
    print(g0)
    # access (not recommended unless you know the key exists)
    print(a[0])
    # get with default value is not supported by Py++
    # default_v: str = a.get(-1, "default value")
    # print(default_v)
    # setting
    a[3] = "d"
    print(a)
    val: str = a.setdefault(4, "e")
    print(val)
    print(a)
    val = a.setdefault(4, "f")
    print(val)
    print(a)
    # setting with mov
    x_key: int = 99
    x_val: str = "z"
    a[mov(x_key)] = mov(x_val)
    print(a)
    val = a.setdefault(mov(x_key), mov(x_val))
    print(val)
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
    # update with mov
    b: dict[int, str] = {6: "y", 7: "w"}
    x_dict: dict[int, str] = {8: "v", 9: "u"}
    b.update(mov(x_dict))
    print(b)
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
    # TODO later: handle addition
    # print({0: 1} | {1: 2})
    # initialize empty
    e: dict[int, int] = {}
    print(e)
    # a nested dict
    f: dict[int, dict[int, int]] = {0: {0: 1}, 1: {0: 1}}
    print(f)
    # modifying references
    f0: dict[int, int] = f[0]
    f0[99] = 98
    print(f)
    f[1][77] = 76
    print(f)
    # inline passing
    _inline_dict({0: 1, 1: 2})
