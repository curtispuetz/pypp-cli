from dataclasses import dataclass
from pathlib import Path

from compy_cli.src.compy_dirs import CompyDirs
from compy_cli.src.main_scripts.util.load_proj_info import load_proj_info
from compy_cli.src.main_scripts.util.load_proj_info import ProjInfo
from compy_cli.src.util.file_changes.calculator import (
    TimeStampsFile,
    get_all_main_py_files,
    get_all_py_files,
    load_previous_timestamps,
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
class WriteCmakeListsFileDeps:
    dirs: CompyDirs
    main_py_files: list[Path]
    proj_info: ProjInfo


@dataclass(frozen=True, slots=True)
class TranspileDeps:
    dirs: CompyDirs
    proj_info: ProjInfo
    src_py_files: list[Path]


@dataclass(frozen=True, slots=True)
class AllData:
    dirs: CompyDirs
    proj_info: ProjInfo
    main_py_files: list[Path]
    src_py_files: list[Path]
    prev_timestamps: TimeStampsFile
    initialize_cpp_project_deps: InitializeCppProjectDeps
    calc_changes_deps: CalcChangesDeps
    write_cmake_lists_file_deps: WriteCmakeListsFileDeps
    transpile_deps: TranspileDeps


def create_all_data(dirs: CompyDirs) -> AllData:
    proj_info: ProjInfo = load_proj_info(dirs)
    main_py_files = create_main_py_files(dirs)
    src_py_files = get_all_py_files(dirs.python_src_dir)
    prev_timestamps = load_previous_timestamps(dirs.timestamps_file)

    return AllData(
        dirs,
        proj_info,
        main_py_files,
        src_py_files,
        prev_timestamps,
        InitializeCppProjectDeps(dirs, proj_info),
        CalcChangesDeps(dirs, proj_info, main_py_files, src_py_files, prev_timestamps),
        WriteCmakeListsFileDeps(dirs, main_py_files, proj_info),
        TranspileDeps(dirs, proj_info, src_py_files),
    )


def create_main_py_files(dirs: CompyDirs) -> list[Path]:
    ret: list[Path] = get_all_main_py_files(dirs.python_dir)
    if not ret:
        raise Exception(
            f"No Python files (*.py) found in '{dirs.python_dir}'. These are the main "
            f"files and at least one is needed."
        )
    return ret
