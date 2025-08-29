from pathlib import Path
import subprocess

from compy_cli.src.compy_dirs import CompyDirs


def get_lib_name_and_version_for_whl_file(whl_file: str) -> tuple[str, str]:
    s = Path(whl_file).name.split("-")
    return s[0], s[1]


def pip_install(pip_str: str, dirs: CompyDirs):
    return _process(pip_str, dirs, "install")


def pip_uninstall(pip_str: str, dirs: CompyDirs):
    return _process(pip_str, dirs, "uninstall")


def _process(pip_str: str, dirs: CompyDirs, s: str):
    print(f"running 'pip {s} {pip_str}'...")
    subprocess.check_call([dirs.calc_py_executable(), "-m", "pip", s, pip_str])
    # Remove timestamps file because changing a library might change how things are
    # transpiled
    if dirs.timestamps_file.exists():
        dirs.timestamps_file.unlink()
