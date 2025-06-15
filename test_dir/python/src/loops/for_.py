def for_loop_fn():
    # looping with 'range()'
    ret: list[int] = [-1]
    for i in range(2, 10, 2):
        ret.append(i)
    print(ret)
