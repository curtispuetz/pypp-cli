from compy_python.ownership import mov


def while_loop_fn():
    print("WHILE LOOP RESULTS:")
    # typical while loop
    a: list[int] = []
    i: int = 0
    while i < 3:
        # Note: I can continue to use the variable i after the mov here because
        #  std::move in C++ does not have any effect on the variable for a primitive
        #  type like int.
        a.append(mov(i))
        i += 1
    print(a)
    # break statement
    while True:
        a.append(mov(i))
        if i > 3:
            break
        i += 1
    print(a)
    # continue statement
    while i < 7:
        if i == 5:
            i += 1
            continue
        a.append(mov(i))
        i += 1
    print(a)
