def set_operations_fn():
    print("SET OPERATIONS RESULTS:")
    a: set[int] = {1, 2, 3}
    if 1 in a:
        print("1 in a")
    if 4 not in a:
        print("4 not in a")
    print(len(a))
    print(min(a))
    print(max(a))

    # TODO later: implement these other set operations
    # print(a | b)
    # print(a & b)
    # print(a - b)
    # print(a ^ b)
