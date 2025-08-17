import json
import os.path
import shutil

from pypp_core.src.config import PyppDirs
from pypp_core.src.main_scripts.util.pip_helper import (
    pip_install_or_uninstall,
)


def pypp_install(library: str, dirs: PyppDirs):
    library_name = pip_install_or_uninstall(library, dirs, install=True)
    # TODO: add some validation that the data in like names_map.json is correct.
    # Remove timestamps file because a new library might change how things are
    # transpiled.
    _copy_cpp_library_files(library_name, dirs)
    _add_installed_library_to_proj_info_json(library_name, dirs)


def _copy_cpp_library_files(library_name: str, dirs: PyppDirs):
    src_dir = dirs.calc_library_cpp_data_dir(library_name)
    dest_dir = dirs.calc_cpp_libs_dir(library_name)
    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)
    shutil.copytree(src_dir, dest_dir)


def _add_installed_library_to_proj_info_json(library_name: str, dirs: PyppDirs):
    with open(dirs.proj_info_file, "r") as f:
        proj_info: dict = json.load(f)
    # TODO: library versions.
    if "installed_libraries" not in proj_info:
        proj_info["installed_libraries"] = [library_name]
    else:
        if library_name not in proj_info["installed_libraries"]:
            proj_info["installed_libraries"].append(library_name)
    with open(dirs.proj_info_file, "w") as f:
        json.dump(proj_info, f, indent=4)
