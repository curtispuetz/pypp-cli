def list_operations_fn():
    print("LIST OPERATIONS RESULTS:")
    a: list[int] = [1, 2, 3]
    if 1 in a:
        print("1 in a")
    if 4 not in a:
        print("4 not in a")
    print(len(a))
    print(a + [4, 5])
    a += [6, 7]
    print(a)
    print([1, 2] * 3)
    a *= 2
    print(a)
    print(min(a))
    print(max(a))
