def set_exceptions_fn():
    print("SET EXCEPTIONS RESULTS:")
    a: set[int] = {1, 2}
    try:
        a.remove(3)
    except KeyError as e:
        print("key error: " + str(e))
