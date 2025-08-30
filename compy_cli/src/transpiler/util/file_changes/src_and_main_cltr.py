from dataclasses import dataclass
from pathlib import Path
from compy_cli.src.transpiler.util.file_changes.cltr import (
    calc_py_file_changes,
    PyFileChanges,
)
from compy_cli.src.transpiler.util.file_changes.file_loader import TimeStampsFile


@dataclass(frozen=True, slots=True)
class FileChangeCltrDeps:
    python_dir: Path
    python_src_dir: Path
    ignored_src_files: list[str]
    ignored_main_files: list[str]
    main_py_files: list[Path]
    src_py_files: list[Path]
    prev_timestamps: TimeStampsFile


class FileChangeCltr:
    def __init__(self, d: FileChangeCltrDeps):
        self._d = d

    def calc_changes(self) -> tuple[PyFileChanges, PyFileChanges]:
        src = calc_py_file_changes(
            self._d.prev_timestamps.src_files,
            self._d.python_src_dir,
            self._d.ignored_src_files,
            self._d.src_py_files,
        )
        main = calc_py_file_changes(
            self._d.prev_timestamps.main_files,
            self._d.python_dir,
            self._d.ignored_main_files,
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
            print(NO_FILE_CHANGES_DETECTED)
        else:
            file_change_print(
                len(src.changed_files) + len(main.changed_files),
                len(src.new_files) + len(main.new_files),
                len(src.deleted_files) + len(main.deleted_files),
                list(src.ignored_file_stems) + list(main.ignored_file_stems),
            )
        return src, main


NO_FILE_CHANGES_DETECTED: str = "No file changes detected."


# TODO: move to a util file
def file_change_print(
    changed_files: int, new_files: int, deleted_files: int, ignored_files: list[str]
):
    print(
        f"changed files: {changed_files}, "
        f"new files: {new_files}, "
        f"deleted files: {deleted_files}, "
        f"ignored files: {ignored_files}"
    )
