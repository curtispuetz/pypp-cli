from pypp_python import auto, defaultdict


def _dict_factory_2() -> dict[int, int]:
    return {1: 2, 3: 4}


def default_dict_create_with_defaults():
    print("DEFAULT DICT CREATION WITH DEFAULTS RESULTS:")
    # creation without specifying a default factory function
    a: auto = defaultdict[int, int](int, {1: 2, 3: 4})
    print(a)
    c: auto = defaultdict[int, float](float, {1: 2.0, 3: 4.0})
    print(c)
    e: auto = defaultdict[int, bool](bool, {1: True, 3: False})
    print(e)
    g: auto = defaultdict[int, str](str, {1: "one", 3: "three"})
    print(g)
    i: auto = defaultdict[int, list[int]](list[int], {1: [1], 3: [3]})
    print(i)
    k: auto = defaultdict[int, dict[int, int]](dict[int, int], {1: {1: 2}, 3: {3: 4}})
    print(k)
    m: auto = defaultdict[int, set[int]](set[int], {1: {1}, 3: {3}})
    print(m)
    # creation with a default factory function
    o: auto = defaultdict[int, int](lambda: 42, {1: 2, 3: 4})
    print(o)
    q: auto = defaultdict[int, float](lambda: 3.14, {1: 2.0, 3: 4.0})
    print(q)
    s: auto = defaultdict[int, bool](lambda: True, {1: True, 3: False})
    print(s)
    u: auto = defaultdict[int, str](lambda: "default", {1: "one", 3: "three"})
    print(u)
    w: auto = defaultdict[int, list[int]](lambda: [1, 2, 3], {1: [1], 3: [3]})
    print(w)
    y: auto = defaultdict[int, dict[int, int]](_dict_factory_2, {1: {1: 2}, 3: {3: 4}})
    print(y)
    aa: auto = defaultdict[int, set[int]](lambda: {1, 2, 3}, {1: {1}, 3: {3}})
    print(aa)
