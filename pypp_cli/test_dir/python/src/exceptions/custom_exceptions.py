from multiprocessing.managers import ValueProxy
from pypp_python import exception


@exception
class CustomException(Exception):
    pass


@exception
class ChildException(CustomException):
    pass


@exception
class _PrivateCustomException(Exception):
    pass


@exception
class CustomValueError(ValueError):
    pass


def custom_exception_fn():
    print("pypp CUSTOM EXCEPTION RESULTS:")
    try:
        raise CustomException("This is a custom exception message.")
    except CustomException as e:
        print("custom exception caught: " + str(e))
    try:
        raise ChildException("This is a child exception message.")
    except ChildException as e:
        print("child exception caught: " + str(e))
    try:
        raise CustomValueError("This is a custom value error message.")
    except ValueError as e:
        print("custom value error caught: " + str(e))
