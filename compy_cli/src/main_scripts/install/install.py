from typing import Callable
import json
from pathlib import Path
import shutil

from compy_cli.src.main_scripts.install.json_validations.always_pass_by_value import (
    validate_always_pass_by_value,
)
from compy_cli.src.main_scripts.install.json_validations.ann_assign_map import (
    validate_ann_assign_map,
)
from compy_cli.src.main_scripts.install.json_validations.attr_map import (
    validate_attr_map,
)
from compy_cli.src.main_scripts.install.json_validations.call_map import (
    validate_call_map,
)
from compy_cli.src.main_scripts.install.json_validations.cmake_lists import (
    validate_cmake_lists,
)
from compy_cli.src.main_scripts.install.json_validations.import_map import (
    validate_import_map,
)
from compy_cli.src.main_scripts.install.json_validations.name_map import (
    validate_name_map,
)
from compy_cli.src.main_scripts.install.json_validations.subscriptable_types import (
    validate_subscriptable_types,
)
from compy_cli.src.main_scripts.util.pip_helper import (
    get_lib_name_and_version_for_whl_file,
    pip_install,
)
from compy_cli.src.compy_dirs import CompyDirs


BRIDGE_JSON_VALIDATION: dict[str, Callable[[object], None]] = {
    "name_map": validate_name_map,
    "ann_assign_map": validate_ann_assign_map,
    "import_map": validate_import_map,
    "call_map": validate_call_map,
    "attr_map": validate_attr_map,
    "subscriptable_types": validate_subscriptable_types,
    "always_pass_by_value": validate_always_pass_by_value,
    "cmake_lists": validate_cmake_lists,
}


def compy_install(library: str, dirs: CompyDirs):
    library_name, version = _get_library_name_and_version(library)
    pip_install(library, dirs)
    try:
        _verify_bridge_json_files(library_name, dirs)
    except AssertionError as e:
        raise AssertionError(
            f"An issue was found in one of the json files for bridge-library "
            f"{library_name}: {e}. "
            f"IMPORTANT: in order to avoid issues, uninstall {library_name}."
        )
    _copy_cpp_library_files_if_any(library_name, dirs)
    _add_installed_library_to_proj_info_json(library_name, version, dirs)


def _verify_bridge_json_files(library_name: str, dirs: CompyDirs):
    for file_name, validate in BRIDGE_JSON_VALIDATION.items():
        json_path: Path = dirs.calc_bridge_json(library_name, file_name)
        if json_path.exists():
            with open(json_path, "r") as f:
                data = json.load(f)
            validate(data)


def _get_library_name_and_version(library: str) -> tuple[str, str]:
    if library.endswith(".whl"):
        return get_lib_name_and_version_for_whl_file(library)
    else:
        if "==" not in library:
            raise ValueError("version must be specified for library")
        s = library.split("==")
        return s[0], s[1]


def _copy_cpp_library_files_if_any(library_name: str, dirs: CompyDirs):
    src_dir = dirs.calc_library_cpp_data_dir(library_name)
    dest_dir = dirs.calc_cpp_libs_dir(library_name)
    if dest_dir.exists():
        shutil.rmtree(dest_dir)
    if src_dir.exists():
        shutil.copytree(src_dir, dest_dir)


def _add_installed_library_to_proj_info_json(
    library_name: str, version: str, dirs: CompyDirs
):
    with open(dirs.proj_info_file, "r") as f:
        proj_info: dict = json.load(f)
    if "installed_bridge_libraries" not in proj_info:
        proj_info["installed_bridge_libraries"] = {library_name: version}
    else:
        if library_name not in proj_info["installed_bridge_libraries"]:
            proj_info["installed_bridge_libraries"][library_name] = version
    with open(dirs.proj_info_file, "w") as f:
        json.dump(proj_info, f, indent=4)
