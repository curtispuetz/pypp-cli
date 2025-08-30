from pathlib import Path
import subprocess


from compy_cli.src.other.compy_paths.package_management import create_py_executable


def compy_uninstall(library: str, target_dir: Path):
    print(f"running 'pip uninstall {library}'...")
    py_executable = create_py_executable(target_dir)
    subprocess.check_call([py_executable, "-m", "pip", "uninstall", library])
