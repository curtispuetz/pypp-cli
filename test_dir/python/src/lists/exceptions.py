def list_exceptions_fn():
    print("LIST EXCEPTIONS RESULTS:")
    a: list[int] = []
    try:
        a.pop()
    except IndexError as e:
        print("index error: " + str(e))
    b: list[int] = [1, 2, 3]
    try:
        b.pop(3)
    except IndexError as e:
        print("index error: " + str(e))
    try:
        b.remove(4)
    except ValueError as e:
        print('value error: ' + str(e))
    try:
        b.index(4)
    except ValueError as e:
        print('value error: ' + str(e))
    try:
        b[3]
    except IndexError as e:
        print("index error: " + str(e))

