from dataclasses import dataclass
from pathlib import Path
from pypp_cli.src.transpilers.other.other.file_changes.cltr import (
    calc_py_file_changes,
    PyFileChanges,
)
from pypp_cli.src.transpilers.other.other.print_results import (
    print_files_changed_results,
)
from pypp_cli.src.transpilers.proj.other.file_loader import (
    TimeStampsFile,
)


@dataclass(frozen=True, slots=True)
class FileChangeCltr:
    _python_dir: Path
    _ignored_files: list[str]
    _py_files: list[Path]
    _prev_timestamps: TimeStampsFile

    def calc_changes(self) -> PyFileChanges:
        changes = calc_py_file_changes(
            self._prev_timestamps.timestamps,
            self._python_dir,
            self._ignored_files,
            self._py_files,
        )

        if not (changes.changed_files or changes.new_files or changes.deleted_files):
            print(NO_FILE_CHANGES_DETECTED)
        else:
            print_files_changed_results(
                len(changes.changed_files),
                len(changes.new_files),
                len(changes.deleted_files),
                list(changes.ignored_file_stems),
            )
        return changes


NO_FILE_CHANGES_DETECTED: str = "No file changes detected."
