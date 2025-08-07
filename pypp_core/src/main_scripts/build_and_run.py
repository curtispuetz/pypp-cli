from pypp_core.src.config import create_test_dir_pypp_dirs
from pypp_core.src.main_scripts.build import pypp_build
from pypp_core.src.main_scripts.run import pypp_run

if __name__ == "__main__":
    pypp_dirs = create_test_dir_pypp_dirs()
    pypp_build(pypp_dirs)
    pypp_run(pypp_dirs)
