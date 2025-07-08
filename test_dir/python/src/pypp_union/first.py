from test_dir.python.pypp.union import Uni, ug, isinst, is_none


def pypp_union_fn():
    print("PYPP UNION RESULTS:")
    a: Uni[int, float] = Uni(3.14)
    if isinst(a, float):
        print(ug(a, float))
    if not isinst(a, int):
        print("a is not an int")
    # Union with None
    b: Uni[int, None] = Uni(None)
    if is_none(b):
        print("b is None")
