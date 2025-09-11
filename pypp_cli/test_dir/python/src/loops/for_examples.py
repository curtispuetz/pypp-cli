def pseudo_fn(integers: list[int], strings: list[str]):
    # typical
    for integer in integers:
        print(integer)
    # with range()
    for i in range(len(integers)):
        print(i)
    for i in range(len(integers), 5, -2):
        print(i)
    # with enumerate()
    for i, val in enumerate(integers):
        print(i, val)
    # with zip()
    for integer, string in zip(integers, strings):
        print(integer, string)
    # with reversed()
    for integer in reversed(integers):
        print(integer)
