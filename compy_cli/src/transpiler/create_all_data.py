from dataclasses import dataclass
from pathlib import Path

from compy_cli.src.bridge_json_path_cltr import BridgeJsonPathCltr
from compy_cli.src.dirs_cltr import CompyDirsCltr
from compy_cli.src.transpiler.util.deleter import CppAndHFileDeleter
from compy_cli.src.transpiler.util.file_changes.src_and_main_cltr import (
    FileChangeCltr,
    FileChangeCltrDeps,
)
from compy_cli.src.transpiler.util.initalize_cpp import (
    CppProjectInitializer,
    CppProjectInitializerDeps,
)
from compy_cli.src.transpiler.util.load_proj_info import load_proj_info
from compy_cli.src.transpiler.util.load_proj_info import ProjInfo
from compy_cli.src.transpiler.util.file_changes.file_loader import (
    TimeStampsFile,
    TimestampsSaver,
    calc_all_main_py_files,
    calc_all_py_files,
    load_previous_timestamps,
)
from compy_cli.src.transpiler.util.transpiler.main_and_src import (
    MainAndSrcTranspiler,
    MainAndSrcTranspilerDeps,
)
from compy_cli.src.transpiler.util.write_cmake_lists import (
    CMakeListsWriter,
    CMakeListsWriterDeps,
)


@dataclass(frozen=True, slots=True)
class AllData:
    proj_info: ProjInfo
    _main_py_files: list[Path]
    src_py_files: list[Path]
    _prev_timestamps: TimeStampsFile
    _cpp_project_initializer_deps: CppProjectInitializerDeps
    cpp_project_initializer: CppProjectInitializer
    _file_change_cltr_deps: FileChangeCltrDeps
    file_change_cltr: FileChangeCltr
    bridge_json_path_cltr: BridgeJsonPathCltr
    _cmake_lists_writer_deps: CMakeListsWriterDeps
    cmake_lists_writer: CMakeListsWriter
    _main_and_src_transpiler_deps: MainAndSrcTranspilerDeps
    main_and_src_transpiler: MainAndSrcTranspiler
    cpp_and_h_file_deleter: CppAndHFileDeleter
    timestamps_saver: TimestampsSaver


def create_all_data(dirs_cltr: CompyDirsCltr) -> AllData:
    proj_info_file: Path = dirs_cltr.calc_proj_info_file()
    cpp_dir: Path = dirs_cltr.calc_cpp_dir()
    cpp_src_dir: Path = dirs_cltr.calc_cpp_src_dir()
    python_dir: Path = dirs_cltr.calc_python_dir()
    python_src_dir: Path = dirs_cltr.calc_python_src_dir()
    timestamps_file: Path = dirs_cltr.calc_timestamps_file()
    proj_info: ProjInfo = load_proj_info(proj_info_file)
    main_py_files = create_main_py_files(python_dir)
    src_py_files = calc_all_py_files(python_src_dir)
    prev_timestamps = load_previous_timestamps(timestamps_file)
    bridge_json_path_cltr = BridgeJsonPathCltr(python_dir)
    cmake_lists_writer_deps = CMakeListsWriterDeps(
        cpp_dir, bridge_json_path_cltr, main_py_files, proj_info.installed_bridge_libs
    )
    file_change_cltr_deps = FileChangeCltrDeps(
        python_dir,
        python_src_dir,
        proj_info.ignored_src_files,
        proj_info.ignored_main_files,
        main_py_files,
        src_py_files,
        prev_timestamps,
    )
    cpp_project_initializer_deps = CppProjectInitializerDeps(
        dirs_cltr.calc_cpp_build_dir(), timestamps_file, proj_info_file, proj_info
    )
    main_and_src_transpiler_deps = MainAndSrcTranspilerDeps(
        cpp_dir,
        python_dir,
        cpp_src_dir,
        python_src_dir,
        proj_info.installed_bridge_libs,
        src_py_files,
        bridge_json_path_cltr,
    )

    return AllData(
        proj_info,
        main_py_files,
        src_py_files,
        prev_timestamps,
        cpp_project_initializer_deps,
        CppProjectInitializer(cpp_project_initializer_deps),
        file_change_cltr_deps,
        FileChangeCltr(file_change_cltr_deps),
        bridge_json_path_cltr,
        cmake_lists_writer_deps,
        CMakeListsWriter(cmake_lists_writer_deps),
        main_and_src_transpiler_deps,
        MainAndSrcTranspiler(main_and_src_transpiler_deps),
        CppAndHFileDeleter(cpp_src_dir),
        TimestampsSaver(timestamps_file),
    )


def create_main_py_files(python_dir: Path) -> list[Path]:
    ret: list[Path] = calc_all_main_py_files(python_dir)
    if not ret:
        raise Exception(
            f"No Python files (*.py) found in '{python_dir}'. These are the main "
            f"files and at least one is needed."
        )
    return ret
