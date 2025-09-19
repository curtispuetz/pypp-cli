from pypp_python import auto, defaultdict


def built_in_set_fn():
    print("BUILT-IN set FUNCTION RESULTS:")
    a: set[int] = {1, 2, 3}
    b: set[int] = set(a)
    a.add(4)
    print(a)
    print(b)
    c: set[int] = set([1, 2, 3])
    print(c)
    d: set[str] = set("hello")
    print(d)
    e: dict[str, int] = {"one": 1, "two": 2}
    f: set[str] = set(e)
    print(f)
    g: set[str] = set[str]()
    print(g)
    h: auto = defaultdict[int, str](str, {1: "one"})
    i: set[int] = set(h)
    print(i)
