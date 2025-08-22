import json
import shutil

from pypp_core.src.main_scripts.util.pip_helper import (
    get_lib_name_and_version_for_whl_file,
    pip_install,
)
from pypp_core.src.pypp_dirs import PyppDirs


def pypp_install(library: str, dirs: PyppDirs):
    library_name, version = _get_library_name_and_version(library)
    pip_install(library, dirs)
    # TODO: add some validation that the data in like name_map.json is correct.
    _copy_cpp_library_files_if_any(library_name, dirs)
    _add_installed_library_to_proj_info_json(library_name, version, dirs)


def _get_library_name_and_version(library: str) -> tuple[str, str]:
    if library.endswith(".whl"):
        return get_lib_name_and_version_for_whl_file(library)
    else:
        if "==" not in library:
            raise ValueError("version must be specified for library")
        s = library.split("==")
        return s[0], s[1]


def _copy_cpp_library_files_if_any(library_name: str, dirs: PyppDirs):
    src_dir = dirs.calc_library_cpp_data_dir(library_name)
    dest_dir = dirs.calc_cpp_libs_dir(library_name)
    if dest_dir.exists():
        shutil.rmtree(dest_dir)
    if src_dir.exists():
        shutil.copytree(src_dir, dest_dir)


def _add_installed_library_to_proj_info_json(
    library_name: str, version: str, dirs: PyppDirs
):
    with open(dirs.proj_info_file, "r") as f:
        proj_info: dict = json.load(f)
    if "installed_libraries" not in proj_info:
        proj_info["installed_libraries"] = {library_name: version}
    else:
        if library_name not in proj_info["installed_libraries"]:
            proj_info["installed_libraries"][library_name] = version
    with open(dirs.proj_info_file, "w") as f:
        json.dump(proj_info, f, indent=4)
