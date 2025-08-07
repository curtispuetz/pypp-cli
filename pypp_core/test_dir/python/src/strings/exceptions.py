def string_exceptions_fn():
    print("STRING EXCEPTIONS RESULTS:")
    s: str = "test"
    try:
        s.index("a")
    except ValueError as e:
        print("value error: " + str(e))
    try:
        s.rindex("a")
    except ValueError as e:
        print("value error: " + str(e))
    try:
        s[9]
    except IndexError as e:
        print("index error: " + str(e))
    try:
        s[-9]
    except IndexError as e:
        print("index error: " + str(e))
