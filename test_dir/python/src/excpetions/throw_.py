def throw_fn():
    # raising an exception and catching all
    try:
        raise Exception("test")
    except Exception:
        print("exception happened")
    # raise an exception and catch specific
    try:
        raise TypeError("test")
    except TypeError:
        print("type error caught")
    # raise an exception and catch specific with the catch value
    try:
        raise TypeError("test")
    except TypeError as e:
        print("type error caught: " + str(e))
    # catch multiple types
    try:
        raise TypeError("test")
    except TypeError:
        print("type error caught")
    except ValueError:
        print("value error caught")
    except Exception:
        print("other error caught")
