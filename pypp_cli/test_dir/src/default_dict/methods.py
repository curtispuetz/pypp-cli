from collections import defaultdict
from pypp_python import auto


def default_dict_methods_fn():
    print("DEFAULT DICT METHODS RESULTS:")
    a: auto = defaultdict[int, str](str)
    a.update({1: "one", 2: "two", 3: "three"})
    # get. Must have a default value.
    print(a.get(4, "four"))
    print(a)
    # setdefault
    print(a.setdefault(5, "five"))
    print(a)
    # pop
    print(a.pop(2))
    print(a)
    # keys
    print(a.keys())
    # values
    print(a.values())
    # items
    print(a.items())
    # clear
    a.clear()
    print(a)
    # copy
    a.update({1: "one", 2: "two", 3: "three"})
    b: auto = a.copy()
    a[4] = "four"
    print(f"original: {a}, default dict after copy: {b}")

    # Creation for defaults
    c: auto = defaultdict[int, int](int, {1: 2, 3: 4})
    print(c)
    d: auto = defaultdict[int, list[str]](
        list[str], {1: ["one", "uno"], 2: ["two", "dos"]}
    )
    print(d)
