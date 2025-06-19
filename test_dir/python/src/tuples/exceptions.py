def tuple_exceptions_fn():
    print("TUPLE EXCEPTIONS RESULTS:")
    a: tuple[int, float, str] = (2, 2.2, "b")
    try:
        a.index(1)
    except ValueError as e:
        print("value error: " + str(e))
    # NOTE: pypp_tg(a, 3) results in a compile error in the C++ rather than a runtime
    # error.
    # try:
    #     pypp_tg(a, 3)
    # except IndexError as e:
    #     print("index error: " + str(e))
