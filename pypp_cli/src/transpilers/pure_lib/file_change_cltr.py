from dataclasses import dataclass
from pathlib import Path
from pypp_cli.src.transpilers.other.other.file_changes.cltr import (
    PyFileChanges,
    calc_py_file_changes,
)
from pypp_cli.src.transpilers.proj.file_change_cltr import (
    NO_FILE_CHANGES_DETECTED,
)
from pypp_cli.src.transpilers.other.other.print_results import (
    print_files_changed_results,
)


@dataclass(frozen=True, slots=True)
class PureFileChangeCltr:
    _root_dir: Path
    _ignored_files: list[str]
    _py_files: list[Path]
    _prev_timestamps: dict[str, float]

    def calc_changes(self) -> PyFileChanges:
        ret = calc_py_file_changes(
            self._prev_timestamps,
            self._root_dir,
            self._ignored_files,
            self._py_files,
        )

        if not (ret.changed_files or ret.new_files or ret.deleted_files):
            print(NO_FILE_CHANGES_DETECTED)
        else:
            print_files_changed_results(
                len(ret.changed_files),
                len(ret.new_files),
                len(ret.deleted_files),
                list(ret.ignored_file_stems),
            )
        return ret
