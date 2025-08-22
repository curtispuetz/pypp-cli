import json
from pathlib import Path

from compy_cli.src.main_scripts.transpiler import Transpiler
from compy_cli.src.compy_dirs import CompyDirs
from compy_cli.src.util.file_change_tracker import (
    calc_py_file_changes,
    get_all_main_py_files,
    get_all_py_files,
    save_timestamps,
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
    with open(dirs.proj_info_file) as file:
        proj_info = json.load(file)
    if proj_info["cpp_dir_is_dirty"]:
        initialize_cpp_project(dirs, proj_info)
    else:
        print("C++ template already copied to the cpp project directory")
    # Step 1.1 write the CmakeLists.txt file
    main_py_files: list[Path] = get_all_main_py_files(dirs.python_dir)
    if not main_py_files:
        raise Exception(f"No Python files (*.py) found in '{dirs.python_dir}'.")
    write_cmake_lists_file(dirs, main_py_files)

    # Step 2: calculate the files that have changed since the last transpile
    src_py_files: list[Path] = get_all_py_files(dirs.python_src_dir)
    py_file_changes, file_timestamps = calc_py_file_changes(
        dirs, proj_info["ignore_src_files"], main_py_files, src_py_files
    )

    # Step 3: iterate over the deleted Py files and delete the corresponding C++ files
    files_deleted: int = 0
    for deleted_file in py_file_changes.deleted_files:
        files_deleted += _delete_cpp_and_h_file(deleted_file, dirs)
    for deleted_file in py_file_changes.changed_files:
        files_deleted += _delete_cpp_and_h_file(deleted_file.rel_path, dirs)

    # Step 4: iterate over the changes and now files and transpile them
    assert dirs.python_src_dir.exists(), "src/ dir must be defined; dir not found"
    dirs.cpp_src_dir.mkdir(parents=True, exist_ok=True)
    transpiler = Transpiler(dirs, proj_info, src_py_files)
    transpiler.transpile_all_changed_files(py_file_changes)

    print(
        f"Compy transpile finished. "
        f"files deleted: {files_deleted}, "
        f"py files transpiled: {transpiler.py_files_transpiled}, "
        f"header files written: {transpiler.header_files_written}, "
        f"cpp files written: {transpiler.cpp_files_written}"
    )

    # Step 5: save the file timestamps
    save_timestamps(file_timestamps, dirs.timestamps_file)

    return transpiler.files_added_or_modified
