import json
from pathlib import Path
from compy_cli.src.pure_lib_transpiler.create_all_data import create_pure_all_data
from compy_cli.src.other.compy_paths.do_pure import DoPureCompyPaths


def compy_transpile_pure(
    paths: DoPureCompyPaths, ignored_files: list[str]
) -> list[Path]:
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
