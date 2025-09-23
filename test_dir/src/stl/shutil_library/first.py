from pypp_python import res_dir
from pypp_python.stl import os, shutil


def shutil_library_fn():
    # shutil.rmtree
    print("Running SHUTIL Library Test")
    resources: str = res_dir()
    new_dir: str = os.path.join(resources, "shutil_lib_results_new_dir")
    os.mkdir(new_dir)
    new_file: str = os.path.join(new_dir, "a.txt")
    with open(new_file, "w") as f:
        f.write("Hello from shutil_library_fn!\n")

    assert os.path.exists(new_dir)
    shutil.rmtree(new_dir)
    assert not os.path.exists(new_dir)
    print("SHUTIL Library Test Passed")
