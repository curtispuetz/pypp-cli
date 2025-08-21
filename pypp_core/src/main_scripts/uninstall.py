import json
import shutil

from pypp_core.src.config import PyppDirs
from pypp_core.src.main_scripts.util.pip_helper import (
    pip_install_or_uninstall,
)


def pypp_uninstall(library: str, dirs: PyppDirs):
    library_name = pip_install_or_uninstall(library, dirs, install=False)
    _delete_cpp_library_files(library_name, dirs)
    _remove_installed_library_to_proj_info_json(library_name, dirs)


def _delete_cpp_library_files(library_name: str, dirs: PyppDirs):
    dest_dir = dirs.calc_cpp_libs_dir(library_name)
    if dest_dir.exists():
        shutil.rmtree(dest_dir)


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
