import subprocess
from pathlib import Path

from pypp_core.src.pypp_dirs import PyppDirs


def pypp_run(dirs: PyppDirs):
    exe_path = Path(dirs.cpp_build_release_dir) / "main.exe"
    print("running generated executable...")
    subprocess.run([str(exe_path)], check=True)
    # TODO later: uncomment this print later maybe
    # print("py++ run finished")
