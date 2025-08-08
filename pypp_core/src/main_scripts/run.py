import subprocess
from pathlib import Path

from pypp_core.src.config import PyppDirs, create_test_dir_pypp_dirs


def pypp_run(dirs: PyppDirs):
    exe_path = Path(dirs.cpp_build_release_dir) / "main.exe"
    print("running generated executable...")
    subprocess.run([str(exe_path)], check=True)
    # TODO later: uncomment this print later maybe
    # print("py++ run finished")


if __name__ == "__main__":
    pypp_run(create_test_dir_pypp_dirs())
