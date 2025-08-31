from dataclasses import dataclass
import json
from pathlib import Path

from compy_cli.src.other.library.json_validations import (
    validate_is_list_of_strings,
)


@dataclass(frozen=True, slots=True)
class PureProjInfo:
    lib_dir_name: str
    ignored_files: list[str]


def load_pure_proj_info(proj_info_file: Path) -> PureProjInfo:
    with open(proj_info_file, "r") as f:
        data = json.load(f)
    _validate_pure_proj_info(data)
    return PureProjInfo(data["lib_dir_name"], data.get("ignore_files", []))


def _validate_pure_proj_info(proj_info: object):
    assert isinstance(proj_info, dict), "proj_info.json must be a JSON Object"
    assert "lib_dir_name" in proj_info, "lib_dir_name key missing in proj_info.json"
    assert isinstance(proj_info["lib_dir_name"], str), (
        "lib_dir_name must be a string in proj_info.json"
    )
    if "ignore_files" in proj_info:
        validate_is_list_of_strings(
            ["ignore_files"], proj_info["ignore_files"], "proj_info"
        )
