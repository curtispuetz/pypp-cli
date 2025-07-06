from test_dir.python.pypp.ownership import mov


def set_of_tuples_fn():
    print("SET OF TUPLES RESULTS:")
    # basic set of tuples
    a: set[tuple[int, int]] = {(1, 2), (3, 4)}
    print(a)
