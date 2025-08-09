import subprocess
import os

from pypp_core.src.config import PyppDirs


def pypp_run_python(file: str, dirs: PyppDirs):
    env = os.environ.copy()
    existing = env.get("PYTHONPATH", "")
    env["PYTHONPATH"] = dirs.python_src_dir + (
        os.pathsep + existing if existing else ""
    )
    subprocess.check_call([dirs.calc_py_executable(), file], env=env)
