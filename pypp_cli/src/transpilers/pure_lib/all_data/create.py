from dataclasses import dataclass
import json
from pathlib import Path

from pypp_cli.src.other.pypp_paths.do_pure import DoPurePyppPaths
from pypp_cli.src.transpilers.pure_lib.all_data.file_change_cltr import PureFileChangeCltr
from pypp_cli.src.transpilers.pure_lib.all_data.transpiler import PureLibTranspiler
from pypp_cli.src.transpilers.other.bridge_libs.path_cltr import (
    BridgeJsonPathCltr,
)
from pypp_cli.src.transpilers.other.bridge_libs.finder import find_libs
from pypp_cli.src.transpilers.other.bridge_libs.verifier import verify_all_bridge_libs
from pypp_cli.src.transpilers.other.deleter import CppAndHFileDeleter
from pypp_cli.src.transpilers.other.file_changes.file_loader import (
    calc_all_py_files,
)


@dataclass(frozen=True, slots=True)
class PureAllData:
    file_change_cltr: PureFileChangeCltr
    cpp_and_h_file_deleter: CppAndHFileDeleter
    transpiler: PureLibTranspiler


def create_pure_all_data(
    paths: DoPurePyppPaths, ignored_files: list[str]
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
