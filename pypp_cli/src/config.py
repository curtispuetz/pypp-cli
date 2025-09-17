from typing import Optional
from pydantic import BaseModel


SHOULDNT_HAPPEN: str = (
    "Shouldn't happen. If you are seeing this, it is a bug. "
    "Please report it at https://github.com/curtispuetz/pypp-cli/issues"
)


class ProjInfo(BaseModel):
    cpp_dir_is_dirty: bool
    namespace: Optional[str]
    override_cpp_write_dir: Optional[str]
    write_metadata_to_dir: Optional[str]
    ignored_files: list[str]
    cmake_minimum_required_version: str


PROJ_INFO_DEFAULTS = ProjInfo(
    cpp_dir_is_dirty=True,
    namespace="me",
    override_cpp_write_dir=None,
    write_metadata_to_dir=None,
    ignored_files=[],
    cmake_minimum_required_version="4.0",
)


class ProjMetadata(BaseModel):
    namespace: str
