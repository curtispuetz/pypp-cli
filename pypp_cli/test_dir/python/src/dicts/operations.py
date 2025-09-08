def dict_operations_fn():
    print("DICT OPERATIONS RESULTS:")
    a: dict[int, str] = {1: "one", 2: "two", 3: "three"}
    if 1 in a:
        print("1 in a")
    if 4 not in a:
        print("4 not in a")
    print(len(a))
    print(min(a))
    print(max(a))

    # TODO later: implement |, |=, and any other operations there are for dict.
