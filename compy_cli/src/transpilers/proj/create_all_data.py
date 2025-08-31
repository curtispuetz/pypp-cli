from dataclasses import dataclass
from pathlib import Path

from compy_cli.src.other.compy_paths.do import DoCompyPaths
from compy_cli.src.transpilers.other.other.bridge_json_path_cltr import (
    BridgeJsonPathCltr,
)
from compy_cli.src.transpilers.proj.bridge_libs.copier import (
    copy_all_lib_cpp_files,
)
from compy_cli.src.transpilers.proj.bridge_libs.deleter import delete_all_cpp_lib_files
from compy_cli.src.transpilers.other.bridge_libs.finder import (
    find_libs,
)
from compy_cli.src.transpilers.proj.bridge_libs.finder import (
    find_added_and_deleted_libs,
)
from compy_cli.src.transpilers.other.bridge_libs.verifier import verify_all_bridge_libs
from compy_cli.src.transpilers.other.other.deleter import CppAndHFileDeleter
from compy_cli.src.transpilers.proj.file_change_cltr import (
    FileChangeCltr,
)
from compy_cli.src.transpilers.proj.other.initalize_cpp import CppProjectInitializer
from compy_cli.src.transpilers.proj.other.load_proj_info import load_proj_info
from compy_cli.src.transpilers.proj.other.load_proj_info import ProjInfo
from compy_cli.src.transpilers.proj.other.file_loader import (
    TimestampsSaver,
    calc_all_main_py_files,
    load_previous_timestamps,
)
from compy_cli.src.transpilers.other.other.file_changes.file_loader import (
    calc_all_py_files,
)
from compy_cli.src.transpilers.proj.transpiler import MainAndSrcTranspiler
from compy_cli.src.transpilers.proj.other.write_cmake_lists import CMakeListsWriter


@dataclass(frozen=True, slots=True)
class AllData:
    cpp_project_initializer: CppProjectInitializer
    file_change_cltr: FileChangeCltr
    cmake_lists_writer: CMakeListsWriter
    main_and_src_transpiler: MainAndSrcTranspiler
    cpp_and_h_file_deleter: CppAndHFileDeleter
    timestamps_saver: TimestampsSaver


def create_all_data(paths: DoCompyPaths) -> AllData:
    proj_info: ProjInfo = load_proj_info(paths.proj_info_file)
    main_py_files = create_main_py_files(paths.python_dir)
    src_py_files = calc_all_py_files(paths.python_src_dir)
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

    return AllData(
        CppProjectInitializer(
            paths.cpp_build_dir, paths.timestamps_file, paths.proj_info_file, proj_info
        ),
        FileChangeCltr(
            paths.python_dir,
            paths.python_src_dir,
            proj_info.ignored_src_files,
            proj_info.ignored_main_files,
            main_py_files,
            src_py_files,
            prev_timestamps,
        ),
        CMakeListsWriter(
            paths.cpp_dir,
            bridge_json_path_cltr,
            main_py_files,
            bridge_libs,
        ),
        MainAndSrcTranspiler(
            paths.cpp_dir,
            paths.python_dir,
            paths.cpp_src_dir,
            paths.python_src_dir,
            bridge_libs,
            src_py_files,
            bridge_json_path_cltr,
        ),
        CppAndHFileDeleter(paths.cpp_src_dir),
        TimestampsSaver(paths.timestamps_file),
    )


def create_main_py_files(python_dir: Path) -> list[Path]:
    ret: list[Path] = calc_all_main_py_files(python_dir)
    if not ret:
        raise Exception(
            f"No Python files (*.py) found in '{python_dir}'. These are the main "
            f"files and at least one is needed."
        )
    return ret
