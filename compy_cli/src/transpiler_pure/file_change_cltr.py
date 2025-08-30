from dataclasses import dataclass
from pathlib import Path
from compy_cli.src.compy_dirs import CompyDirs
from compy_cli.src.transpiler.util.file_changes.cltr import (
    PyFileChanges,
    calc_py_file_changes,
)
from compy_cli.src.transpiler.util.file_changes.src_and_main_cltr import (
    NO_FILE_CHANGES_DETECTED,
    file_change_print,
)
from compy_cli.src.transpiler_pure.transpile import PureProjInfo


# TODO: prune deps for this one and other one.
@dataclass(frozen=True, slots=True)
class PureFileChangeCltrDeps:
    dirs: CompyDirs
    proj_info: PureProjInfo
    py_files: list[Path]
    prev_timestamps: dict[str, float]


class PureFileChangeCltr:
    def __init__(self, d: PureFileChangeCltrDeps):
        self._d = d

    def calc_changes(self) -> PyFileChanges:
        ret = calc_py_file_changes(
            self._d.prev_timestamps,
            self._d.dirs.calc_pure_lib_dir(self._d.proj_info.lib_dir_name),
            self._d.proj_info.ignored_files,
            self._d.py_files,
        )

        if not (ret.changed_files or ret.new_files or ret.deleted_files):
            print(NO_FILE_CHANGES_DETECTED)
        else:
            file_change_print(
                len(ret.changed_files),
                len(ret.new_files),
                len(ret.deleted_files),
                list(ret.ignored_file_stems),
            )
        return ret
