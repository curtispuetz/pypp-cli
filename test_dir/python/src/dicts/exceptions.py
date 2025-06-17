from test_dir.python.pypp.dict_get import pypp_dg


def dict_exceptions_fn():
    print("DICT EXCEPTIONS RESULTS:")
    a: dict[int, int] = {0: 1, 1: 2}
    try:
        a.pop(-1)
    except KeyError as e:
        print("key error: " + str(e))
    try:
        pypp_dg(a, -1)
    except KeyError as e:
        print("key error: " + str(e))