import json
import os
import subprocess

from pypp_core.src.config import PyppDirs


def pypp_install(library: str, dirs: PyppDirs):
    print(f"running 'pip install {library}'...")
    python_executable = os.path.join(dirs.python_dir, ".venv", "Scripts", "python.exe")
    print(f"using python executable: {python_executable}")
    subprocess.check_call([python_executable, "-m", "pip", "install", library])
    _add_installed_library_to_proj_info_json(library, dirs)


def _add_installed_library_to_proj_info_json(library: str, dirs: PyppDirs):
    with open(dirs.proj_info_file, "r") as f:
        proj_info: dict = json.load(f)
    # TODO: library versions.
    if "installed_libraries" not in proj_info:
        proj_info["installed_libraries"] = [library]
    else:
        if library not in proj_info["installed_libraries"]:
            proj_info["installed_libraries"].append(library)
    with open(dirs.proj_info_file, "w") as f:
        json.dump(proj_info, f, indent=4)
