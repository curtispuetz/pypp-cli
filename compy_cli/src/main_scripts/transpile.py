from pathlib import Path

from compy_cli.src.compy_dirs import CompyDirs
from compy_cli.src.util.transpiler import Transpiler
from compy_cli.src.main_scripts.util.load_proj_info import load_proj_info
from compy_cli.src.main_scripts.util.load_proj_info import ProjInfo
from compy_cli.src.util.file_changes.calculator import (
    get_all_main_py_files,
    get_all_py_files,
    save_timestamps,
)
from compy_cli.src.util.file_changes.file_change_tracker_2 import FileChangeTracker
from compy_cli.src.util.file_changes.calculator import (
    TimeStampsFile,
    load_previous_timestamps,
)
from compy_cli.src.util.initalize_cpp import (
    initialize_cpp_project,
)
from compy_cli.src.util.write_cmake_lists import write_cmake_lists_file


def _delete_cpp_and_h_file(filepath: Path, dirs: CompyDirs) -> int:
    files_deleted: int = 0
    cpp_file: Path = filepath.with_suffix(".cpp")
    h_file: Path = filepath.with_suffix(".h")
    cpp_full_path: Path = dirs.cpp_src_dir / cpp_file
    h_full_path: Path = dirs.cpp_src_dir / h_file
    if cpp_full_path.exists():
        cpp_full_path.unlink()
        files_deleted += 1
    if h_full_path.exists():
        h_full_path.unlink()
        files_deleted += 1
    return files_deleted


def compy_transpile(dirs: CompyDirs) -> list[Path]:
    # Step 1: Copy the C++ template to the cpp project directory if marked as dirty
    proj_info: ProjInfo = load_proj_info(dirs)
    if proj_info.cpp_dir_is_dirty:
        initialize_cpp_project(dirs, proj_info)
    else:
        print("C++ template already copied to the cpp project directory")

    # Step 2: calculate the files that have changed since the last transpile
    main_py_files: list[Path] = get_all_main_py_files(dirs.python_dir)
    if not main_py_files:
        raise Exception(f"No Python files (*.py) found in '{dirs.python_dir}'.")

    src_py_files: list[Path] = get_all_py_files(dirs.python_src_dir)
    prev_timestamps: TimeStampsFile = load_previous_timestamps(dirs.timestamps_file)
    fct_src = FileChangeTracker(prev_timestamps.src_files)
    fct_main = FileChangeTracker(prev_timestamps.main_files)
    src_changes = fct_src.calc_py_file_changes(
        dirs.python_src_dir, proj_info.ignored_src_files, src_py_files
    )
    main_changes = fct_main.calc_py_file_changes(
        dirs.python_dir, proj_info.ignored_main_files, main_py_files
    )

    if not (
        src_changes.changed_files
        or src_changes.new_files
        or src_changes.deleted_files
        or main_changes.changed_files
        or main_changes.new_files
        or main_changes.deleted_files
    ):
        print("No file changes detected.")
    else:
        print(
            f"changed files: {
                len(src_changes.changed_files) + len(main_changes.changed_files)
            }, "
            f"new files: {len(src_changes.new_files) + len(main_changes.new_files)}, "
            f"deleted files: {
                len(src_changes.deleted_files) + len(main_changes.deleted_files)
            },"
            f" ignored files: {
                list(src_changes.ignored_file_stems)
                + list(main_changes.ignored_file_stems)
            }"
        )

    # Step 2.1 write the CMakeLists.txt file
    write_cmake_lists_file(
        dirs, main_py_files, proj_info, main_changes.ignored_file_stems
    )

    # Step 3: iterate over the deleted Py files and delete the corresponding C++ files
    files_deleted: int = 0
    for files in [
        src_changes.deleted_files,
        main_changes.deleted_files,
        src_changes.changed_files,
        main_changes.changed_files,
    ]:
        for file in files:
            files_deleted += _delete_cpp_and_h_file(file, dirs)

    # Step 4: iterate over the changes and new files and transpile them
    assert dirs.python_src_dir.exists(), "src/ dir must be defined; dir not found"
    dirs.cpp_src_dir.mkdir(parents=True, exist_ok=True)
    src_transpiler = Transpiler(dirs, proj_info, src_py_files)
    src_transpiler.transpile_all_changed_files(
        src_changes.new_files, src_changes.changed_files
    )
    main_transpiler = Transpiler(dirs, proj_info, src_py_files, is_main_files=True)
    main_transpiler.transpile_all_changed_files(
        main_changes.new_files, main_changes.changed_files
    )

    print(
        f"Compy transpile finished. "
        f"files deleted: {files_deleted}, "
        f"py files transpiled: "
        f"{src_transpiler.py_files_transpiled + main_transpiler.py_files_transpiled}, "
        f"header files written: "
        f"{src_transpiler.header_files_written + main_transpiler.header_files_written},"
        f" cpp files written: "
        f"{src_transpiler.cpp_files_written + main_transpiler.cpp_files_written}"
    )

    # Step 5: save the file timestamps
    save_timestamps(
        TimeStampsFile(main_changes.new_timestamps, src_changes.new_timestamps),
        dirs.timestamps_file,
    )

    return (
        src_transpiler.files_added_or_modified + main_transpiler.files_added_or_modified
    )
