def for_loop_fn():
    # looping with 'range()'
    # TODO: fix the issue where lists can't be initialized empty. Check the same for
    #  the other types like set, dict, and string
    ret: list[int] = [-1]
    for i in range(2, 10, 2):
        ret.append(i)
    print(ret)
