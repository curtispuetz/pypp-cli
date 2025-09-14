import json
from pathlib import Path

from pypp_cli.src.config import PROJ_INFO_DEFAULTS, ProjInfo
from pypp_cli.src.other.library.json_validations import (
    validate_is_list_of_strings,
)


def load_proj_info(proj_info_file: Path) -> ProjInfo:
    with open(proj_info_file) as file:
        proj_info = json.load(file)
    _validate_proj_info(proj_info)
    return ProjInfo(
        proj_info["cpp_dir_is_dirty"],
        proj_info.get("ignore_src_files", PROJ_INFO_DEFAULTS.ignored_src_files),
        proj_info.get("ignore_main_files", PROJ_INFO_DEFAULTS.ignored_main_files),
        proj_info.get(
            "cmake_minimum_required_version",
            PROJ_INFO_DEFAULTS.cmake_minimum_required_version,
        ),
    )


def _validate_proj_info(proj_info: object):
    assert isinstance(proj_info, dict), "proj_info.json must be a JSON Object"
    assert "cpp_dir_is_dirty" in proj_info, (
        "cpp_dir_is_dirty key missing in proj_info.json"
    )
    assert isinstance(proj_info["cpp_dir_is_dirty"], bool), (
        "cpp_dir_is_dirty must be a boolean in proj_info.json"
    )
    if "ignore_src_files" in proj_info:
        validate_is_list_of_strings(
            ["ignore_src_files"], proj_info["ignore_src_files"], "proj_info"
        )
    if "ignore_main_files" in proj_info:
        validate_is_list_of_strings(
            ["ignore_main_files"], proj_info["ignore_main_files"], "proj_info"
        )
    if "cmake_minimum_required_version" in proj_info:
        assert isinstance(proj_info["cmake_minimum_required_version"], str), (
            "cmake_minimum_required_version must be a string in proj_info.json"
        )
