import json
from pathlib import Path
import shutil


from compy_cli.src.dirs_cltr import CompyDirsCltr
from compy_cli.src.package_manager.util.pip_helper import (
    PipHelper,
    PipHelperDeps,
    get_lib_name_and_version_for_whl_file,
)


def compy_uninstall(library: str, dirs_cltr: CompyDirsCltr):
    library_name = _get_library_name(library)
    pip_helper = PipHelper(
        PipHelperDeps(dirs_cltr.calc_py_executable(), dirs_cltr.calc_timestamps_file())
    )
    pip_helper.uninstall(library)
    _delete_cpp_library_files(library_name, dirs_cltr)
    _remove_installed_library_to_proj_info_json(
        library_name, dirs_cltr.calc_proj_info_file()
    )


def _get_library_name(library: str) -> str:
    if library.endswith(".whl"):
        return get_lib_name_and_version_for_whl_file(library)[0]
    else:
        return library


def _delete_cpp_library_files(library_name: str, dirs_cltr: CompyDirsCltr):
    dest_dir = dirs_cltr.calc_cpp_libs_dir(library_name)
    if dest_dir.exists():
        shutil.rmtree(dest_dir)


def _remove_installed_library_to_proj_info_json(library: str, proj_info_file: Path):
    with open(proj_info_file, "r") as f:
        proj_info: dict = json.load(f)
    if (
        "installed_bridge_libraries" in proj_info
        and library in proj_info["installed_bridge_libraries"]
    ):
        del proj_info["installed_bridge_libraries"][library]
    with open(proj_info_file, "w") as f:
        json.dump(proj_info, f, indent=4)
