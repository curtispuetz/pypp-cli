from dataclasses import dataclass
from pathlib import Path

from compy_cli.src.compy_dirs import CompyDirs
from compy_cli.src.transpiler.util.transpiler import Transpiler, TranspilerDeps
from compy_cli.src.transpiler.util.load_proj_info import load_proj_info
from compy_cli.src.transpiler.util.load_proj_info import ProjInfo
from compy_cli.src.transpiler.util.file_changes.file_loader import (
    TimeStampsFile,
    calc_all_main_py_files,
    calc_all_py_files,
    load_previous_timestamps,
)
from compy_cli.src.transpiler.util.write_cmake_lists import (
    CMakeListsWriter,
    CMakeListsWriterDeps,
)


@dataclass(frozen=True, slots=True)
class InitializeCppProjectDeps:
    dirs: CompyDirs
    proj_info: ProjInfo


@dataclass(frozen=True, slots=True)
class CalcChangesDeps:
    dirs: CompyDirs
    proj_info: ProjInfo
    main_py_files: list[Path]
    src_py_files: list[Path]
    prev_timestamps: TimeStampsFile


@dataclass(frozen=True, slots=True)
class AllData:
    dirs: CompyDirs
    proj_info: ProjInfo
    main_py_files: list[Path]
    src_py_files: list[Path]
    prev_timestamps: TimeStampsFile
    initialize_cpp_project_deps: InitializeCppProjectDeps
    calc_changes_deps: CalcChangesDeps
    cmake_lists_writer_deps: CMakeListsWriterDeps
    cmake_lists_writer: CMakeListsWriter
    transpiler_deps: TranspilerDeps
    transpiler: Transpiler


def create_all_data(dirs: CompyDirs) -> AllData:
    proj_info: ProjInfo = load_proj_info(dirs)
    main_py_files = create_main_py_files(dirs)
    src_py_files = calc_all_py_files(dirs.python_src_dir)
    prev_timestamps = load_previous_timestamps(dirs.timestamps_file)
    transpiler_deps = TranspilerDeps(dirs, proj_info, src_py_files)
    cmake_lists_writer_deps = CMakeListsWriterDeps(dirs, main_py_files, proj_info)

    return AllData(
        dirs,
        proj_info,
        main_py_files,
        src_py_files,
        prev_timestamps,
        InitializeCppProjectDeps(dirs, proj_info),
        CalcChangesDeps(dirs, proj_info, main_py_files, src_py_files, prev_timestamps),
        cmake_lists_writer_deps,
        CMakeListsWriter(cmake_lists_writer_deps),
        transpiler_deps,
        Transpiler(transpiler_deps),
    )


def create_main_py_files(dirs: CompyDirs) -> list[Path]:
    ret: list[Path] = calc_all_main_py_files(dirs.python_dir)
    if not ret:
        raise Exception(
            f"No Python files (*.py) found in '{dirs.python_dir}'. These are the main "
            f"files and at least one is needed."
        )
    return ret
