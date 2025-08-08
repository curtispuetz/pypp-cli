import json
import os
import subprocess

from pypp_core.src.config import PyppDirs


def pypp_uninstall(library: str, dirs: PyppDirs):
    print(f"running 'pip uninstall {library}'...")
    python_executable = os.path.join(dirs.python_dir, ".venv", "Scripts", "python.exe")
    subprocess.check_call([python_executable, "-m", "pip", "uninstall", library])
    _remove_installed_library_to_proj_info_json(library, dirs)


def _remove_installed_library_to_proj_info_json(library: str, dirs: PyppDirs):
    with open(dirs.proj_info_file, "r") as f:
        proj_info: dict = json.load(f)
    if (
        "installed_libraries" in proj_info
        and library in proj_info["installed_libraries"]
    ):
        proj_info["installed_libraries"].remove(library)
    with open(dirs.proj_info_file, "w") as f:
        json.dump(proj_info, f, indent=4)
