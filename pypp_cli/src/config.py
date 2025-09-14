from dataclasses import dataclass


SHOULDNT_HAPPEN: str = (
    "Shouldn't happen. If you are seeing this, it is a bug. "
    "Please report it at https://github.com/curtispuetz/pypp-cli/issues"
)


@dataclass(slots=True)
class ProjInfo:
    cpp_dir_is_dirty: bool
    ignored_src_files: list[str]
    ignored_main_files: list[str]
    cmake_minimum_required_version: str


PROJ_INFO_DEFAULTS = ProjInfo(
    cpp_dir_is_dirty=True,
    ignored_src_files=[],
    ignored_main_files=[],
    cmake_minimum_required_version="4.0",
)


@dataclass(frozen=True, slots=True)
class PureProjInfo:
    lib_dir_name: str
    ignored_files: list[str]


PURE_PROJ_INFO_DEFAULTS = PureProjInfo(lib_dir_name="easter_egg", ignored_files=[])
