import subprocess
from pathlib import Path
import sys


def pypp_run(cpp_build_release_dir: Path, exe_name: str | None):
    exe_path = cpp_build_release_dir / f"{exe_name}"
    if sys.platform == "win32":
        exe_path = exe_path.with_suffix(".exe")
    print("running generated executable...")
    subprocess.check_call([str(exe_path)])
    # TODO later: uncomment this print later maybe
    # print("Py++ run finished")
