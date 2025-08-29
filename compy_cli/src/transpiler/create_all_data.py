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


# TODO: maybe make the 'deps' private? because I don't need to access them elsewhere.
#  and also maybe some of the other ones too.
@dataclass(frozen=True, slots=True)
class AllData:
    dirs: CompyDirs
    proj_info: ProjInfo
    main_py_files: list[Path]
    src_py_files: list[Path]
    prev_timestamps: TimeStampsFile
    cpp_project_initializer_deps: CppProjectInitializerDeps
    cpp_project_initializer: CppProjectInitializer
    file_change_cltr_deps: FileChangeCltrDeps
    file_change_cltr: FileChangeCltr
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
    file_change_cltr_deps = FileChangeCltrDeps(
        dirs, proj_info, main_py_files, src_py_files, prev_timestamps
    )
    cpp_project_initializer_deps = CppProjectInitializerDeps(dirs, proj_info)

    return AllData(
        dirs,
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
