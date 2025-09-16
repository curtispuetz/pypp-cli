from src.constants import C, MyConfig2


def imports_test_fn2():
    print("IMPORTS TEST RESULTS 2:")
    # showing this twice to ensure no linker errors
    print(C)
    print(MyConfig2.a, MyConfig2.b)
