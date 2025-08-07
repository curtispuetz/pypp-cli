from pypp_core.src.main_scripts.format import pypp_format
from pypp_core.src.main_scripts.transpile import pypp_transpile

if __name__ == "__main__":
    files_added_or_modified = pypp_transpile()
    pypp_format(files_added_or_modified)
