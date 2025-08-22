import json
import shutil

from compy_cli.src.main_scripts.util.pip_helper import (
    get_lib_name_and_version_for_whl_file,
    pip_uninstall,
)
from compy_cli.src.compy_dirs import CompyDirs


def pypp_uninstall(library: str, dirs: CompyDirs):
    library_name = _get_library_name(library)
    pip_uninstall(library, dirs)
    _delete_cpp_library_files(library_name, dirs)
    _remove_installed_library_to_proj_info_json(library_name, dirs)


def _get_library_name(library: str) -> str:
    if library.endswith(".whl"):
        return get_lib_name_and_version_for_whl_file(library)[0]
    else:
        return library


def _delete_cpp_library_files(library_name: str, dirs: CompyDirs):
    dest_dir = dirs.calc_cpp_libs_dir(library_name)
    if dest_dir.exists():
        shutil.rmtree(dest_dir)


def _remove_installed_library_to_proj_info_json(library: str, dirs: CompyDirs):
    with open(dirs.proj_info_file, "r") as f:
        proj_info: dict = json.load(f)
    if (
        "installed_libraries" in proj_info
        and library in proj_info["installed_libraries"]
    ):
        del proj_info["installed_libraries"][library]
    with open(dirs.proj_info_file, "w") as f:
        json.dump(proj_info, f, indent=4)
