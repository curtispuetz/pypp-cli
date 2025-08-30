import subprocess
import os

from compy_cli.src.dirs_cltr import CompyDirsCltr


def compy_run_python(file: str, dirs_cltr: CompyDirsCltr):
    env = os.environ.copy()
    existing = env.get("PYTHONPATH", "")
    env["PYTHONPATH"] = str(dirs_cltr.calc_python_src_dir()) + (
        os.pathsep + existing if existing else ""
    )
    subprocess.check_call([dirs_cltr.calc_py_executable(), file], env=env)
