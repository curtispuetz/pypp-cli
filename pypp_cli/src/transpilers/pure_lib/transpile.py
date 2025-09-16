import json
from pathlib import Path
from pypp_cli.src.transpilers.pure_lib.all_data.create import create_pure_all_data
from pypp_cli.src.other.pypp_paths.do_pure import DoPurePyppPaths


def pypp_transpile_pure(paths: DoPurePyppPaths, ignored_files: list[str]) -> list[Path]:
    a = create_pure_all_data(paths, ignored_files)

    changes = a.file_change_cltr.calc_changes()
    files_deleted: int = a.cpp_and_h_file_deleter.delete_files(
        [changes.deleted_files, changes.changed_files]
    )
    ret = a.transpiler.transpile(changes, files_deleted)
    _save_timestamps(paths.timestamps_file, changes.new_timestamps)

    return ret


def _save_timestamps(timestamps_file: Path, new_timestamps: dict[str, float]):
    with open(timestamps_file, "w") as f:
        json.dump(new_timestamps, f, indent=2)
