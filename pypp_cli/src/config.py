from dataclasses import dataclass


SHOULDNT_HAPPEN: str = (
    "Shouldn't happen. If you are seeing this, it is a bug. "
    "Please report it at https://github.com/curtispuetz/pypp-cli/issues"
)


@dataclass(slots=True)
class ProjInfo:
    cpp_dir_is_dirty: bool
    ignored_files: list[str]
    cmake_minimum_required_version: str


PROJ_INFO_DEFAULTS = ProjInfo(
    cpp_dir_is_dirty=True,
    ignored_files=[],
    cmake_minimum_required_version="4.0",
)
