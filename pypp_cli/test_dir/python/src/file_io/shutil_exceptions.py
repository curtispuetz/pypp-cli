import shutil
from pypp_python import pypp_get_resources


def shutil_exceptions_fn():
    print("SHUTIL EXCEPTIONS RESULTS:")
    try:
        shutil.rmtree(pypp_get_resources("test_doesn't_exist"))
    except FileNotFoundError as e:
        print("caught FileNotFoundError: ", e)

    try:
        shutil.rmtree(pypp_get_resources("test_is_here.txt"))
    except NotADirectoryError as e:
        print("caught NotADirectoryError: " + str(e))

    # Be careful with this one that you actually don't have permission to
    # delete the folder.
    # try:
    #     shutil.rmtree(r"C:\Users\puetz\PycharmProjects\bridge-lib-glfw")
    # except PermissionError as e:
    #     print("caught PermissionError: " + str(e))
