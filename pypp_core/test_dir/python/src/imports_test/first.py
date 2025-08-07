from constants import C, MyConfig2


def imports_test_fn():
    print("IMPORTS TEST RESULTS:")
    # just showing that you can actually import a constant variable from a different
    # file
    print(C)
    print(MyConfig2.a, MyConfig2.b)
