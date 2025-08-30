import json
from pathlib import Path
import shutil

from compy_cli.src.bridge_json_path_cltr import BridgeJsonPathCltr
from compy_cli.src.dirs_cltr import CompyDirsCltr
from compy_cli.src.package_manager.installer.json_verifier import BridgeJsonVerifier
from compy_cli.src.package_manager.util.pip_helper import (
    PipHelper,
    get_lib_name_and_version_for_whl_file,
)


def compy_install(library: str, dirs_cltr: CompyDirsCltr):
    library_name, version = _get_library_name_and_version(library)
    pip_helper = PipHelper(
        dirs_cltr.calc_py_executable(), dirs_cltr.calc_timestamps_file()
    )
    pip_helper.install(library)
    bridge_json_verifier = BridgeJsonVerifier(
        BridgeJsonPathCltr(dirs_cltr.calc_python_dir()), library_name
    )
    bridge_json_verifier.verify_bridge_jsons()
    _copy_cpp_library_files_if_any(library_name, dirs_cltr)
    _add_installed_library_to_proj_info_json(
        library_name, version, dirs_cltr.calc_proj_info_file()
    )


def _get_library_name_and_version(library: str) -> tuple[str, str]:
    if library.endswith(".whl"):
        return get_lib_name_and_version_for_whl_file(library)
    else:
        if "==" not in library:
            raise ValueError("version must be specified for library")
        s = library.split("==")
        return s[0], s[1]


def _copy_cpp_library_files_if_any(library_name: str, dirs_cltr: CompyDirsCltr):
    src_dir = dirs_cltr.calc_library_cpp_data_dir(library_name)
    dest_dir = dirs_cltr.calc_cpp_libs_dir(library_name)
    if dest_dir.exists():
        shutil.rmtree(dest_dir)
    if src_dir.exists():
        shutil.copytree(src_dir, dest_dir)


def _add_installed_library_to_proj_info_json(
    library_name: str, version: str, proj_info_file: Path
):
    with open(proj_info_file, "r") as f:
        proj_info: dict = json.load(f)
    if "installed_bridge_libraries" not in proj_info:
        proj_info["installed_bridge_libraries"] = {library_name: version}
    else:
        if library_name not in proj_info["installed_bridge_libraries"]:
            proj_info["installed_bridge_libraries"][library_name] = version
    with open(proj_info_file, "w") as f:
        json.dump(proj_info, f, indent=4)
