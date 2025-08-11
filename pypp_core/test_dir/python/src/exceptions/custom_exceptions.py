from pypp_python.exceptionclass import exception


@exception
class CustomException(Exception):
    pass

@exception
class ChildException(CustomException):
    pass


def custom_exception_fn():
    print("PYPP CUSTOM EXCEPTION RESULTS:")
    try:
        raise CustomException("This is a custom exception message.")
    except CustomException as e:
        print("custom exception caught: " + str(e))
    try:
        raise ChildException("This is a child exception message.")
    except ChildException as e:
        print("child exception caught: " + str(e))
