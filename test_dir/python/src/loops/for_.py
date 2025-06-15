def for_loop_fn():
    # looping with 'range()'
    ret: list[int] = []
    for i in range(2, 10, 2):
        ret.append(i)
    print(ret)
    # looping over a list
    a: list[int] = []
    for val in ret:
        a.append(val)
    print(a)
    # looping over a set
    b: set[int] = {10, 20, 30}
    for val in b:
        a.append(val)
    print(a)
