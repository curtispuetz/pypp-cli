from src.main_scripts.build import pypp_build
from src.main_scripts.format import pypp_format
from src.main_scripts.run import pypp_run
from src.main_scripts.transpile import pypp_transpile

if __name__ == "__main__":
    files_added_or_modified = pypp_transpile()
    pypp_format(files_added_or_modified)
    pypp_build()
    pypp_run()
