import json
from pathlib import Path
from compy_cli.src.pure_lib_transpiler.file_change_cltr import PureFileChangeCltr
from compy_cli.src.pure_lib_transpiler.transpiler import PureLibTranspiler
from compy_cli.src.transpiler.util.deleter import CppAndHFileDeleter
from compy_cli.src.transpiler.util.file_changes.file_loader import calc_all_py_files
from compy_cli.src.other.compy_paths.do_pure import DoPureCompyPaths


def load_pure_previous_timestamps(timestamps_file: Path) -> dict[str, float]:
    if timestamps_file.exists():
        with open(timestamps_file, "r") as f:
            data = json.load(f)
        return data
    return {}


def compy_transpile_pure(
    paths: DoPureCompyPaths, ignored_files: list[str]
) -> list[Path]:
    py_files: list[Path] = calc_all_py_files(paths.python_dir)
    prev_timestamps: dict[str, float] = load_pure_previous_timestamps(
        paths.timestamps_file
    )
    pure_file_change_cltr = PureFileChangeCltr(
        paths.python_dir,
        ignored_files,
        py_files,
        prev_timestamps,
    )
    changes = pure_file_change_cltr.calc_changes()

    cpp_and_h_file_deleter = CppAndHFileDeleter(paths.cpp_dir)
    files_deleted: int = cpp_and_h_file_deleter.delete_files(
        [changes.deleted_files, changes.changed_files]
    )

    t = PureLibTranspiler(
        paths.python_dir, paths.cpp_dir, paths.site_packages_dir, py_files
    )
    ret = t.transpile(changes, files_deleted)

    with open(paths.timestamps_file, "w") as f:
        json.dump(
            changes.new_timestamps,
            f,
            indent=2,
        )

    return ret
