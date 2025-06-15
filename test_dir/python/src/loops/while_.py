def while_loop_fn():
    a: list[int] = []
    i: int = 0
    while i < 3:
        a.append(i)
        i += 1
    print(a)
