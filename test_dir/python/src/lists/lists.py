def list_fn():
    a: list[int] = [1, 2, 3, 4, 5]
    print(a)
    a[0] = 10
    print(a)
    a.append(11)
    print(a)
    print(str(a[-1]))
    b: int = a[-1]
    b = 20
    print(str(b))
    print(a)
