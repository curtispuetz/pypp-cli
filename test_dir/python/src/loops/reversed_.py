from test_dir.python.pypp.ownership import mov


def reversed_fn():
    print("REVERSED RESULTS:")
    # over a list
    a: list[int] = []
    for x in reversed([1, 2, 3]):
        y: int = x
        a.append(mov(y))
    print(a)
    # over a string
    b: list[str] = []
    for x in reversed("abcd"):
        y: str = x
        b.append(mov(y))
    print(b)
    # with zip
    for x, z in zip(reversed([1, 2, 3]), reversed("abc")):
        print(f"{x}, {z}")
