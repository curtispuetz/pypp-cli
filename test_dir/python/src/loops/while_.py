def while_loop_fn():
    # typical while loop
    a: list[int] = []
    i: int = 0
    while i < 3:
        a.append(i)
        i += 1
    print(a)
    # break statement
    while True:
        a.append(i)
        if i > 3:
            break
        i += 1
    print(a)
    # continue statement
    while i < 7:
        if i == 5:
            i += 1
            continue
        a.append(i)
        i += 1
    print(a)
