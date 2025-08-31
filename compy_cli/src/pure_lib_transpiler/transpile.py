import json
from pathlib import Path
from compy_cli.src.pure_lib_transpiler.file_change_cltr import PureFileChangeCltr
from compy_cli.src.pure_lib_transpiler.transpiler import PureLibTranspiler
from compy_cli.src.transpiler.bridge_json_path_cltr import BridgeJsonPathCltr
from compy_cli.src.transpiler.bridge_libs.finder import find_bridge_libs
from compy_cli.src.transpiler.bridge_libs.verifier import verify_all_bridge_libs
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

    bridge_libs = find_bridge_libs(paths.site_packages_dir)
    bridge_json_path_cltr = BridgeJsonPathCltr(paths.site_packages_dir)
    verify_all_bridge_libs(bridge_libs, bridge_json_path_cltr)
    # Note: not removing timestamps file here because users can just do that themselves
    # if they want that.

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
        paths.python_dir, paths.cpp_dir, py_files, bridge_json_path_cltr, bridge_libs
    )
    ret = t.transpile(changes, files_deleted)

    with open(paths.timestamps_file, "w") as f:
        json.dump(
            changes.new_timestamps,
            f,
            indent=2,
        )

    return ret
