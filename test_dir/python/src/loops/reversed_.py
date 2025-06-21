def reversed_fn():
    print("REVERSED RESULTS:")
    # over a list
    a: list[int] = []
    for x in reversed([1, 2, 3]):
        a.append(x)
    print(a)
    # over a string
    b: list[str] = []
    for x in reversed("abcd"):
        b.append(x)
    print(b)
    # with zip
    for x, z in zip(reversed([1, 2, 3]), reversed("abc")):
        print(f"{x}, {z}")
