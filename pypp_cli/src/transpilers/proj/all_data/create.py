from dataclasses import dataclass
from pathlib import Path

from pypp_cli.src.config import ProjInfo
from pypp_cli.src.other.pypp_paths.do import DoPyppPaths, DoTranspileDeps
from pypp_cli.src.transpilers.library.bridge_libs.path_cltr import (
    BridgeJsonPathCltr,
)
from pypp_cli.src.transpilers.library.file_tracker import PyFilesTracker
from pypp_cli.src.transpilers.proj.all_data.bridge_libs.copier import (
    copy_all_lib_cpp_files,
)
from pypp_cli.src.transpilers.library.bridge_libs.finder import (
    PyppLibsData,
    find_libs,
)
from pypp_cli.src.transpilers.proj.all_data.bridge_libs.finder import (
    find_new_libs,
)
from pypp_cli.src.transpilers.library.bridge_libs.verifier import (
    verify_all_bridge_jsons,
)
from pypp_cli.src.transpilers.library.deleter import CppAndHFileDeleter
from pypp_cli.src.transpilers.proj.all_data.file_change_cltr import (
    FileChangeCltr,
)
from pypp_cli.src.transpilers.proj.all_data.initalize_cpp import CppProjectInitializer
from pypp_cli.src.transpilers.proj.all_data.timestamps import (
    TimestampsSaver,
    load_previous_timestamps,
)
from pypp_cli.src.transpilers.library.file_changes.file_loader import (
    calc_all_py_files,
)
from pypp_cli.src.transpilers.proj.all_data.metadata_saver import MetadataSaver
from pypp_cli.src.transpilers.proj.all_data.transpiler import MainAndSrcTranspiler
from pypp_cli.src.transpilers.proj.all_data.write_cmake_lists import CMakeListsWriter


@dataclass(frozen=True, slots=True)
class AllData:
    cpp_project_initializer: CppProjectInitializer
    file_change_cltr: FileChangeCltr
    cmake_lists_writer: CMakeListsWriter
    main_and_src_transpiler: MainAndSrcTranspiler
    cpp_and_h_file_deleter: CppAndHFileDeleter
    timestamps_saver: TimestampsSaver
    metadata_saver: MetadataSaver
    py_files_tracker: PyFilesTracker


def create_all_data(transpile_deps: DoTranspileDeps) -> AllData:
    paths: DoPyppPaths = transpile_deps.paths
    proj_info: ProjInfo = transpile_deps.proj_info
    py_files = calc_all_py_files(paths.python_dir)
    bridge_json_path_cltr = BridgeJsonPathCltr(paths.site_packages_dir)

    libs_data: PyppLibsData = find_libs(paths.site_packages_dir)
    new_libs = find_new_libs(paths.cpp_dir, libs_data.libs)
    # Note: not removing deleted libraries. I guess users will do that themselves.
    # I could provide CLI commands to delete libraries.
    bridge_json_models = verify_all_bridge_jsons(libs_data.libs, bridge_json_path_cltr)
    copy_all_lib_cpp_files(paths.cpp_libs_dir, paths.site_packages_dir, new_libs)
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
            libs_data.libs,
            proj_info.cmake_minimum_required_version,
            py_files_tracker,
        ),
        MainAndSrcTranspiler(
            proj_info.namespace,
            paths.cpp_dir,
            paths.python_dir,
            libs_data,
            py_files,
            bridge_json_path_cltr,
            bridge_json_models,
            paths.proj_bridge_json_dir,
            py_files_tracker,
        ),
        CppAndHFileDeleter(paths.cpp_dir),
        TimestampsSaver(paths.timestamps_file, py_files_tracker),
        MetadataSaver(
            proj_info.write_metadata_to_dir, proj_info.namespace, paths.python_dir
        ),
        py_files_tracker,
    )
