from pathlib import Path
import subprocess

from pypp_cli.src.other.pypp_paths.package_management import create_py_executable


def pypp_install(library: str, target_dir: Path):
    print(f"running 'pip install {library}'...")
    py_executable = create_py_executable(target_dir)
    subprocess.check_call([py_executable, "-m", "pip", "install", library])
