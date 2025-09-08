from pypp_python import int_list, float_list, str_list


def list_declaration_fn():
    print("LIST DECLARATION RESULTS:")
    # empty
    a: list[int] = []
    print(a)
    # with some initial values
    b: list[int] = [1, 2, 3, 4, 5]
    print(b)
    # with repeated values
    c: list[int] = [1, 2, 3] * 5
    print(c)
    # int_list, float_list, str_list
    d: list[int] = int_list(10)
    print(d)
    e: list[float] = float_list(5)
    print(e)
    f: list[str] = str_list(3)
    print(f)
    # int_list, float_list, str_list with initial values
    g: list[int] = int_list(10, 99)
    print(g)
    h: list[float] = float_list(5, 1.1)
    print(h)
    i: list[str] = str_list(3, "hello")
    print(i)
