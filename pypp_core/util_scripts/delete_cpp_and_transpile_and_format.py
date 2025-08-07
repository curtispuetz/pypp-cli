import os
import shutil

from pypp_core.src.config import create_test_dir_pypp_dirs
from pypp_core.src.main_scripts.format import pypp_format
from pypp_core.src.main_scripts.transpile import pypp_transpile

if __name__ == "__main__":
    dirname: str = os.path.dirname(__file__)
    shutil.rmtree(os.path.join(dirname, "..", "test_dir", "cpp"))
    pypp_dirs = create_test_dir_pypp_dirs()
    files_added_or_modified = pypp_transpile(pypp_dirs)
    pypp_format(files_added_or_modified, pypp_dirs)
