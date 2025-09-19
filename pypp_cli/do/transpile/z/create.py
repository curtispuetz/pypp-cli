from dataclasses import dataclass
from pathlib import Path

from pypp_cli.do.transpile.calc_file_changes.node import FileChangeCltr
from pypp_cli.do.transpile.find_libs.node import find_libs
from pypp_cli.do.transpile.timestamps.node import (
    TimestampsSaver,
    load_previous_timestamps,
)
from pypp_cli.y.proj_info import ProjInfo
from pypp_cli.do.z.paths.do import DoPyppPaths, DoTranspileDeps
from pypp_cli.do.transpile.y.py_file_tracker import PyFilesTracker
from pypp_cli.do.transpile.copy_lib_cpp.node import (
    copy_all_lib_cpp_files,
)
from pypp_cli.do.transpile.load_transpiler_config.node import (
    load_transpiler_config,
)
from pypp_cli.do.transpile.delete_cpp_files.node import CppAndHFileDeleter
from pypp_cli.do.transpile.init_cpp_proj.node import CppProjectInitializer
from pypp_cli.do.transpile.z.py_files_cltr import (
    calc_all_py_files,
)
from pypp_cli.do.transpile.metadata.node import MetadataSaver
from pypp_cli.do.transpile.transpile.node import MainAndSrcTranspiler
from pypp_cli.do.transpile.write_cmake_lists.node import CMakeListsWriter


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

    libs_data, new_libs = find_libs(paths.site_packages_dir, paths.cpp_dir)
    # Note: not removing deleted libraries. I guess users will do that themselves.
    # I could provide CLI commands to delete libraries.
    transpiler_config_models = load_transpiler_config(
        libs_data.libs, paths.site_packages_dir, paths.proj_transpiler_config_dir
    )
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
            libs_data.libs,
            proj_info.cmake_minimum_required_version,
            py_files_tracker,
            transpiler_config_models,
        ),
        MainAndSrcTranspiler(
            proj_info.namespace,
            paths.cpp_dir,
            paths.python_dir,
            libs_data,
            py_files,
            transpiler_config_models,
            py_files_tracker,
        ),
        CppAndHFileDeleter(paths.cpp_dir),
        TimestampsSaver(paths.timestamps_file, py_files_tracker),
        MetadataSaver(
            proj_info.write_metadata_to_dir, proj_info.namespace, paths.python_dir
        ),
        py_files_tracker,
    )
