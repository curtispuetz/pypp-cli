from test_dir.python.pypp.union import Uni, vg, isinst


def pypp_union_fn():
    print("PYPP UNION RESULTS:")
    a: Uni[int, float] = Uni(3.14)
    if isinst(a, float):
        print(vg(a, float))
    if not isinst(a, int):
        print("a is not an int")
    # TODO: be able to use None in Uni.
