import os
import subprocess

from pypp_cli.util_scripts.calling_cli.util import calc_test_dir_python_executable

dirname: str = os.path.dirname(__file__)
if __name__ == "__main__":
    # TODO later: Fix because this command is deleted
    main_file = os.path.join(dirname, "../../test_dir/python/main.py")
    python_executable = calc_test_dir_python_executable()
    src_files = os.path.join(dirname, "../../test_dir/python/src")
    env = os.environ.copy()
    env["PYTHONPATH"] = src_files + os.pathsep + env.get("PYTHONPATH", "")
    subprocess.check_call([python_executable, main_file], env=env)
