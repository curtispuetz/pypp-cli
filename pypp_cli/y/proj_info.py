from typing import Optional

from pydantic import BaseModel


class ProjInfo(BaseModel):
    namespace: str
    override_cpp_write_dir: Optional[str]
    write_metadata_to_dir: Optional[str]
    ignored_files: list[str]
    cmake_minimum_required_version: str
    cpp_dir_is_dirty: bool
