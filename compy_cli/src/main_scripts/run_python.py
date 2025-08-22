import subprocess
import os

from compy_cli.src.compy_dirs import CompyDirs


def pypp_run_python(file: str, dirs: CompyDirs):
    env = os.environ.copy()
    existing = env.get("PYTHONPATH", "")
    env["PYTHONPATH"] = str(dirs.python_src_dir) + (
        os.pathsep + existing if existing else ""
    )
    subprocess.check_call([dirs.calc_py_executable(), file], env=env)
