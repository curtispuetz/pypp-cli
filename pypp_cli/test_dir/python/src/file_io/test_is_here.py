from pypp_python import pypp_get_resource_dir
import os


def test_is_here_fn():
    print("FILE IO TEST IS HERE RESULTS:")
    # NOTE: This works for the C++ only if the executable is in the first level of
    # the build/ dir
    resources_dir: str = pypp_get_resource_dir()
    file: str = os.path.join(resources_dir, "test_is_here.txt")
    if os.path.isfile(file):
        print("test_is_here.txt file exists")
    else:
        raise Exception("test_is_here.txt file does not exist")
