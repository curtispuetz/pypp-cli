from dataclasses import dataclass
import json
from pathlib import Path

from compy_cli.src.package_manager.installer.json_validations.util.validations import (
    validate_is_list_of_strings,
)


@dataclass(frozen=True, slots=True)
class ProjInfo:
    cpp_dir_is_dirty: bool
    ignored_src_files: list[str]
    ignored_main_files: list[str]


def load_proj_info(proj_info_file: Path) -> ProjInfo:
    with open(proj_info_file) as file:
        proj_info = json.load(file)
    _validate_proj_info(proj_info)
    return ProjInfo(
        proj_info["cpp_dir_is_dirty"],
        proj_info.get("ignore_src_files", []),
        proj_info.get("ignore_main_files", []),
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
