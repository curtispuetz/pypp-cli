from dataclasses import dataclass
from pathlib import Path

from compy_cli.src.compy_dirs import CompyDirs
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
    _cmake_lists_writer_deps: CMakeListsWriterDeps
    cmake_lists_writer: CMakeListsWriter
    _main_and_src_transpiler_deps: MainAndSrcTranspilerDeps
    main_and_src_transpiler: MainAndSrcTranspiler


def create_all_data(dirs: CompyDirs) -> AllData:
    proj_info: ProjInfo = load_proj_info(dirs.proj_info_file)
    main_py_files = create_main_py_files(dirs.python_dir)
    src_py_files = calc_all_py_files(dirs.python_src_dir)
    prev_timestamps = load_previous_timestamps(dirs.timestamps_file)
    cmake_lists_writer_deps = CMakeListsWriterDeps(dirs, main_py_files, proj_info)
    file_change_cltr_deps = FileChangeCltrDeps(
        dirs.python_dir,
        dirs.python_src_dir,
        proj_info.ignored_src_files,
        proj_info.ignored_main_files,
        main_py_files,
        src_py_files,
        prev_timestamps,
    )
    cpp_project_initializer_deps = CppProjectInitializerDeps(
        dirs.cpp_build_dir,
        dirs.timestamps_file,
        dirs.proj_info_file,
        proj_info.ignored_src_files,
        proj_info.ignored_main_files,
        proj_info.installed_bridge_libs,
    )
    main_and_src_transpiler_deps = MainAndSrcTranspilerDeps(
        dirs.cpp_dir,
        dirs.python_dir,
        dirs.cpp_src_dir,
        dirs.python_src_dir,
        proj_info.installed_bridge_libs,
        src_py_files,
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
        cmake_lists_writer_deps,
        CMakeListsWriter(cmake_lists_writer_deps),
        main_and_src_transpiler_deps,
        MainAndSrcTranspiler(main_and_src_transpiler_deps),
    )


def create_main_py_files(python_dir: Path) -> list[Path]:
    ret: list[Path] = calc_all_main_py_files(python_dir)
    if not ret:
        raise Exception(
            f"No Python files (*.py) found in '{python_dir}'. These are the main "
            f"files and at least one is needed."
        )
    return ret
