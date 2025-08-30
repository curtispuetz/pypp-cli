import subprocess

from compy_cli.src.dirs_cltr import CompyDirsCltr


def compy_install(library: str, dirs_cltr: CompyDirsCltr):
    print(f"running 'pip install {library}'...")
    subprocess.check_call(
        [dirs_cltr.calc_py_executable(), "-m", "pip", "install", library]
    )
