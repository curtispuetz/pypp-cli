from exceptions.custom_exceptions import ChildException


def test_all_exceptions_fn():
    print("ALL EXCEPTIONS TEST RESULTS:")
    # TODO: add the others. But first they all need to inherit from Exception
    exceptions: list[Exception] = [
        Exception("test"),
        ValueError("test"),
        IndexError("test"),
        KeyError("test"),
        AssertionError("test"),
        RuntimeError("test"),
        NotImplementedError("test"),
        OSError("test"),
        FileNotFoundError("test"),
        NotADirectoryError("test"),
        PermissionError("test"),
        FileExistsError("test"),
    ]
    for exc in exceptions:
        try:
            raise exc
        except Exception as e:
            print("caught exception: " + str(e))

    # also test importing another exception
    try:
        raise ChildException("test")
    except ChildException as e:
        print("caught exception: " + str(e))
