from pathlib import Path
import subprocess
import os

from compy_cli.src.other.compy_paths.run_python import create_run_python_paths


def compy_run_python(file: str, target_dir: Path):
    paths = create_run_python_paths(target_dir)
    env = os.environ.copy()
    existing = env.get("PYTHONPATH", "")
    env["PYTHONPATH"] = str(paths.python_src_dir) + (
        os.pathsep + existing if existing else ""
    )
    subprocess.check_call([paths.py_executable, file], env=env)
