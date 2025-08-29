from dataclasses import dataclass
from pathlib import Path
from compy_cli.src.compy_dirs import CompyDirs
from compy_cli.src.transpiler.util.file_changes.cltr import (
    calc_py_file_changes,
    PyFileChanges,
)
from compy_cli.src.transpiler.util.file_changes.file_loader import TimeStampsFile
from compy_cli.src.transpiler.util.load_proj_info import ProjInfo


@dataclass(frozen=True, slots=True)
class FileChangeCltrDeps:
    dirs: CompyDirs
    proj_info: ProjInfo
    main_py_files: list[Path]
    src_py_files: list[Path]
    prev_timestamps: TimeStampsFile


class FileChangeCltr:
    def __init__(self, d: FileChangeCltrDeps):
        self._d = d

    def calc_changes(self) -> tuple[PyFileChanges, PyFileChanges]:
        src = calc_py_file_changes(
            self._d.prev_timestamps.src_files,
            self._d.dirs.python_src_dir,
            self._d.proj_info.ignored_src_files,
            self._d.src_py_files,
        )
        main = calc_py_file_changes(
            self._d.prev_timestamps.main_files,
            self._d.dirs.python_dir,
            self._d.proj_info.ignored_main_files,
            self._d.main_py_files,
        )

        if not (
            src.changed_files
            or src.new_files
            or src.deleted_files
            or main.changed_files
            or main.new_files
            or main.deleted_files
        ):
            print("No file changes detected.")
        else:
            print(
                f"changed files: {len(src.changed_files) + len(main.changed_files)}, "
                f"new files: {len(src.new_files) + len(main.new_files)}, "
                f"deleted files: {len(src.deleted_files) + len(main.deleted_files)},"
                f" ignored files: {
                    list(src.ignored_file_stems) + list(main.ignored_file_stems)
                }"
            )
        return src, main
