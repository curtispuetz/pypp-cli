from dataclasses import dataclass
from pathlib import Path

from compy_cli.src.other.compy_paths.do import DoCompyPaths
from compy_cli.src.transpiler.bridge_json_path_cltr import BridgeJsonPathCltr
from compy_cli.src.transpiler.bridge_libs.copier import copy_all_bridge_lib_cpp_files
from compy_cli.src.transpiler.bridge_libs.deleter import delete_all_bridge_lib_cpp_files
from compy_cli.src.transpiler.bridge_libs.finder import (
    find_added_and_deleted_bridge_libs,
    find_bridge_libs,
)
from compy_cli.src.transpiler.bridge_libs.verifier import verify_all_bridge_libs
from compy_cli.src.transpiler.util.deleter import CppAndHFileDeleter
from compy_cli.src.transpiler.util.file_changes.src_and_main_cltr import FileChangeCltr
from compy_cli.src.transpiler.util.initalize_cpp import CppProjectInitializer
from compy_cli.src.transpiler.util.load_proj_info import load_proj_info
from compy_cli.src.transpiler.util.load_proj_info import ProjInfo
from compy_cli.src.transpiler.util.file_changes.file_loader import (
    TimeStampsFile,
    TimestampsSaver,
    calc_all_main_py_files,
    calc_all_py_files,
    load_previous_timestamps,
)
from compy_cli.src.transpiler.util.transpiler.main_and_src import MainAndSrcTranspiler
from compy_cli.src.transpiler.util.write_cmake_lists import CMakeListsWriter


@dataclass(frozen=True, slots=True)
class AllData:
    proj_info: ProjInfo
    _main_py_files: list[Path]
    src_py_files: list[Path]
    _prev_timestamps: TimeStampsFile
    cpp_project_initializer: CppProjectInitializer
    file_change_cltr: FileChangeCltr
    bridge_json_path_cltr: BridgeJsonPathCltr
    cmake_lists_writer: CMakeListsWriter
    main_and_src_transpiler: MainAndSrcTranspiler
    cpp_and_h_file_deleter: CppAndHFileDeleter
    timestamps_saver: TimestampsSaver


def create_all_data(paths: DoCompyPaths) -> AllData:
    proj_info: ProjInfo = load_proj_info(paths.proj_info_file)
    main_py_files = create_main_py_files(paths.python_dir)
    src_py_files = calc_all_py_files(paths.python_src_dir)
    bridge_json_path_cltr = BridgeJsonPathCltr(paths.site_packages_dir)

    bridge_libs = find_bridge_libs(paths.site_packages_dir)
    new_bridge_libs, deleted_bridge_libs = find_added_and_deleted_bridge_libs(
        paths.cpp_dir, set(bridge_libs)
    )
    delete_all_bridge_lib_cpp_files(paths.cpp_dir, deleted_bridge_libs)
    verify_all_bridge_libs(new_bridge_libs, bridge_json_path_cltr)
    copy_all_bridge_lib_cpp_files(
        paths.cpp_dir, paths.site_packages_dir, new_bridge_libs
    )
    # Should remove the timestamps file because transpiling can be different with a
    # new bridge library.
    if (
        len(new_bridge_libs) > 0 or len(deleted_bridge_libs) > 0
    ) and paths.timestamps_file.exists():
        print("removing file_timestamps.json because bridge-libraries have changed")
        paths.timestamps_file.unlink()

    prev_timestamps = load_previous_timestamps(paths.timestamps_file)

    return AllData(
        proj_info,
        main_py_files,
        src_py_files,
        prev_timestamps,
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
        bridge_json_path_cltr,
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
