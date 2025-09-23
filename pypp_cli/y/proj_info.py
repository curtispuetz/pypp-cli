import json
from pathlib import Path
from typing import Optional

from pydantic import BaseModel, ValidationError


class ProjInfo(BaseModel):
    namespace: str
    override_cpp_write_dir: Optional[str]
    write_metadata_to_dir: Optional[str]
    ignored_files: list[str]
    cmake_minimum_required_version: str
    cpp_dir_is_dirty: bool


def load_proj_info(proj_info_file: Path) -> ProjInfo:
    with open(proj_info_file) as file:
        proj_info = json.load(file)
    try:
        return ProjInfo(**proj_info)
    except ValidationError as e:
        raise ValueError(f"Issue found in proj_info.json file: {e}") from e
