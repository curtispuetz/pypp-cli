def built_in_list_fn():
    print("BUILT-IN LIST FUNCTION RESULTS:")
    a: list[int] = [1, 2, 3]
    b: list[int] = list(a)
    a.append(4)
    print(a)
    print(b)
    c: list[int] = list({1, 2, 3})
    print(c)
    d: list[str] = list("hello")
    print(d)
    e: dict[str, int] = {"one": 1, "two": 2}
    f: list[str] = list(e)
    print(f)
    g: list[str] = list[str]()
    print(g)
