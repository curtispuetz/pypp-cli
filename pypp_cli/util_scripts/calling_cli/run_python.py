import os
import subprocess

from pypp_cli.util_scripts.calling_cli.util import calc_test_dir_python_executable

dirname: str = os.path.dirname(__file__)
if __name__ == "__main__":
    main_file = os.path.join(dirname, "../../test_dir/main.py")
    python_executable = calc_test_dir_python_executable()
    subprocess.check_call([python_executable, main_file])
