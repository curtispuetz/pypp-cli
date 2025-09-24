import subprocess
from pathlib import Path
import sys


def _calc_exe_path(root_dir: Path, exe_name: str) -> Path:
    exe_path = root_dir / f"{exe_name}"
    if sys.platform == "win32":
        exe_path = exe_path.with_suffix(".exe")
    return exe_path


def pypp_run(cpp_build_release_dir: Path, exe_name: str):
    exe_path = _calc_exe_path(cpp_build_release_dir, exe_name)
    if not exe_path.is_file():
        raise FileNotFoundError(f"Executable '{exe_name}' not found in cpp build dir")

    print(f"running '{exe_name}' executable...")
    subprocess.check_call([str(exe_path)])
    # TODO later: uncomment this print later maybe
    # print("Py++ run finished")
