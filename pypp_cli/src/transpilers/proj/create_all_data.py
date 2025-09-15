from dataclasses import dataclass
from pathlib import Path

from pypp_cli.src.config import ProjInfo
from pypp_cli.src.other.pypp_paths.do import DoPyppPaths
from pypp_cli.src.transpilers.other.other.bridge_json_path_cltr import (
    BridgeJsonPathCltr,
)
from pypp_cli.src.transpilers.other.other.file_tracker import PyFilesTracker
from pypp_cli.src.transpilers.proj.bridge_libs.copier import (
    copy_all_lib_cpp_files,
)
from pypp_cli.src.transpilers.proj.bridge_libs.deleter import delete_all_cpp_lib_files
from pypp_cli.src.transpilers.other.bridge_libs.finder import (
    find_libs,
)
from pypp_cli.src.transpilers.proj.bridge_libs.finder import (
    find_added_and_deleted_libs,
)
from pypp_cli.src.transpilers.other.bridge_libs.verifier import verify_all_bridge_libs
from pypp_cli.src.transpilers.other.other.deleter import CppAndHFileDeleter
from pypp_cli.src.transpilers.proj.file_change_cltr import (
    FileChangeCltr,
)
from pypp_cli.src.transpilers.proj.other.initalize_cpp import CppProjectInitializer
from pypp_cli.src.transpilers.proj.other.load_proj_info import load_proj_info
from pypp_cli.src.transpilers.proj.other.file_loader import (
    TimestampsSaver,
    calc_all_main_py_files,
    load_previous_timestamps,
)
from pypp_cli.src.transpilers.other.other.file_changes.file_loader import (
    calc_all_py_files,
)
from pypp_cli.src.transpilers.proj.transpiler import MainAndSrcTranspiler
from pypp_cli.src.transpilers.proj.other.write_cmake_lists import CMakeListsWriter


@dataclass(frozen=True, slots=True)
class AllData:
    cpp_project_initializer: CppProjectInitializer
    file_change_cltr: FileChangeCltr
    cmake_lists_writer: CMakeListsWriter
    main_and_src_transpiler: MainAndSrcTranspiler
    cpp_and_h_file_deleter: CppAndHFileDeleter
    timestamps_saver: TimestampsSaver
    py_files_tracker: PyFilesTracker


def create_all_data(paths: DoPyppPaths) -> AllData:
    proj_info: ProjInfo = load_proj_info(paths.proj_info_file)
    py_files = calc_all_py_files(paths.python_dir)
    bridge_json_path_cltr = BridgeJsonPathCltr(paths.site_packages_dir)

    bridge_libs, pure_libs = find_libs(paths.site_packages_dir)
    new_bridge_libs, new_pure_libs, deleted_libs = find_added_and_deleted_libs(
        paths.cpp_dir, bridge_libs, pure_libs
    )
    delete_all_cpp_lib_files(paths.cpp_dir, deleted_libs)
    verify_all_bridge_libs(new_bridge_libs, bridge_json_path_cltr)
    copy_all_lib_cpp_files(
        paths.cpp_dir, paths.site_packages_dir, new_bridge_libs, new_pure_libs
    )
    # Note: not removing timestamps file here because users can just do that themselves
    # if they want that.

    prev_timestamps = load_previous_timestamps(paths.timestamps_file)

    py_files_tracker = PyFilesTracker(
        py_files, {Path(f) for f in prev_timestamps.main_files}
    )

    return AllData(
        CppProjectInitializer(
            paths.cpp_dir, paths.timestamps_file, paths.proj_info_file, proj_info
        ),
        FileChangeCltr(
            paths.python_dir,
            proj_info.ignored_files,
            py_files,
            prev_timestamps,
        ),
        CMakeListsWriter(
            paths.cpp_dir,
            bridge_json_path_cltr,
            bridge_libs,
            proj_info.cmake_minimum_required_version,
            py_files_tracker,
        ),
        MainAndSrcTranspiler(
            paths.cpp_dir,
            paths.python_dir,
            bridge_libs,
            py_files,
            bridge_json_path_cltr,
            py_files_tracker,
        ),
        CppAndHFileDeleter(paths.cpp_dir),
        TimestampsSaver(paths.timestamps_file, py_files_tracker),
        py_files_tracker,
    )


# TODO now: delete this and calc_all_main_py_files
def create_main_py_files(python_dir: Path) -> list[Path]:
    ret: list[Path] = calc_all_main_py_files(python_dir)
    if not ret:
        raise ValueError(
            f"No Python files (*.py) found in '{python_dir}'. These are the main "
            f"files with a main block and at least one is needed."
        )
    return ret
