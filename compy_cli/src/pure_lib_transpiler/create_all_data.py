from dataclasses import dataclass
import json
from pathlib import Path

from compy_cli.src.other.compy_paths.do_pure import DoPureCompyPaths
from compy_cli.src.pure_lib_transpiler.file_change_cltr import PureFileChangeCltr
from compy_cli.src.pure_lib_transpiler.transpiler import PureLibTranspiler
from compy_cli.src.transpiler.bridge_json_path_cltr import BridgeJsonPathCltr
from compy_cli.src.transpiler.bridge_libs.finder import find_libs
from compy_cli.src.transpiler.bridge_libs.verifier import verify_all_bridge_libs
from compy_cli.src.transpiler.util.deleter import CppAndHFileDeleter
from compy_cli.src.transpiler.util.file_changes.file_loader import calc_all_py_files


@dataclass(frozen=True, slots=True)
class PureAllData:
    file_change_cltr: PureFileChangeCltr
    cpp_and_h_file_deleter: CppAndHFileDeleter
    transpiler: PureLibTranspiler


def create_pure_all_data(
    paths: DoPureCompyPaths, ignored_files: list[str]
) -> PureAllData:
    py_files: list[Path] = calc_all_py_files(paths.python_dir)
    bridge_libs, _ = find_libs(paths.site_packages_dir)
    bridge_json_path_cltr = BridgeJsonPathCltr(paths.site_packages_dir)
    verify_all_bridge_libs(bridge_libs, bridge_json_path_cltr)
    # Note: not removing timestamps file here because users can just do that themselves
    # if they want that.

    prev_timestamps = _load_pure_previous_timestamps(paths.timestamps_file)

    return PureAllData(
        PureFileChangeCltr(
            paths.python_dir,
            ignored_files,
            py_files,
            prev_timestamps,
        ),
        CppAndHFileDeleter(paths.cpp_dir),
        PureLibTranspiler(
            paths.python_dir,
            paths.cpp_dir,
            py_files,
            bridge_json_path_cltr,
            bridge_libs,
        ),
    )


def _load_pure_previous_timestamps(timestamps_file: Path) -> dict[str, float]:
    if timestamps_file.exists():
        with open(timestamps_file, "r") as f:
            data = json.load(f)
        return data
    return {}
