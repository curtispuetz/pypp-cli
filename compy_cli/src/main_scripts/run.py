import subprocess
from pathlib import Path

from compy_cli.src.compy_dirs import CompyDirs


def compy_run(dirs: CompyDirs):
    exe_path = Path(dirs.cpp_build_release_dir) / "main.exe"
    print("running generated executable...")
    subprocess.run([str(exe_path)], check=True)
    # TODO later: uncomment this print later maybe
    # print("Compy run finished")
