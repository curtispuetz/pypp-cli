from collections import defaultdict
from pypp_python import auto


def default_dict_operations_fn():
    print("DEFAULT DICT OPERATIONS RESULTS:")
    a: auto = defaultdict[int, str](str)
    a.update({1: "one", 2: "two", 3: "three"})
    if 1 in a:
        print("1 in a")
    if 4 not in a:
        print("4 not in a")
    print(len(a))
    print(min(a))
    print(max(a))
    b: dict[int, str] = {1: "one", 2: "two", 3: "three"}
    # note: when comparing defaultdict with dict, the default dict must be on the left
    # side of the comparison or a compilation error occurs.
    if a == b:
        print("is equal")
    c: dict[int, str] = {1: "one", 2: "two", 3: "thee"}
    if a != c:
        print("is not equal")
