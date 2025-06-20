import os
import shutil

from src.main_scripts.format import pypp_format
from src.main_scripts.transpile import pypp_transpile

if __name__ == "__main__":
    dirname: str = os.path.dirname(__file__)
    shutil.rmtree(os.path.join(dirname, "..", "test_dir", "cpp"))
    pypp_transpile()
    pypp_format()
