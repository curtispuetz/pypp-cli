from dataclasses import dataclass
from pathlib import Path
from compy_cli.src.transpilers.other.other.file_changes.cltr import (
    calc_py_file_changes,
    PyFileChanges,
)
from compy_cli.src.transpilers.other.other.print_results import (
    print_files_changed_results,
)
from compy_cli.src.transpilers.proj.other.file_loader import (
    TimeStampsFile,
)


@dataclass(frozen=True, slots=True)
class FileChangeCltr:
    _python_dir: Path
    _python_src_dir: Path
    _ignored_src_files: list[str]
    _ignored_main_files: list[str]
    _main_py_files: list[Path]
    _src_py_files: list[Path]
    _prev_timestamps: TimeStampsFile

    def calc_changes(self) -> tuple[PyFileChanges, PyFileChanges]:
        src = calc_py_file_changes(
            self._prev_timestamps.src_files,
            self._python_src_dir,
            self._ignored_src_files,
            self._src_py_files,
        )
        main = calc_py_file_changes(
            self._prev_timestamps.main_files,
            self._python_dir,
            self._ignored_main_files,
            self._main_py_files,
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
            print_files_changed_results(
                len(src.changed_files) + len(main.changed_files),
                len(src.new_files) + len(main.new_files),
                len(src.deleted_files) + len(main.deleted_files),
                list(src.ignored_file_stems) + list(main.ignored_file_stems),
            )
        return src, main


NO_FILE_CHANGES_DETECTED: str = "No file changes detected."
