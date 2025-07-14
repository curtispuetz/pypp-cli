import ast
import os
import shutil

from src.config import (
    C_PYTHON_SRC_DIR,
    C_CPP_DIR,
    C_CPP_BUILD_DIR,
    C_CPP_SRC_DIR,
)
from src.constants import SECRET_MAIN_FILE_DIR_PREFIX
from src.util.file_change_tracker import (
    calc_py_file_changes,
    save_timestamps,
)
from src.util.initalize_cpp import initialize_cpp_project
from src.util.get_py import get_main_py_ast_tree, get_src_py_ast_tree
from src.util.main_source import calc_main_cpp_source, calc_src_file_cpp_and_h_source
from src.util.write_cmake_lists import write_cmake_lists_file


def _delete_cpp_and_h_file(filepath: str) -> int:
    files_deleted = 0
    file_without_ext = filepath[:-3]  # Remove the .py extension
    cpp_file = file_without_ext + ".cpp"
    h_file = file_without_ext + ".h"
    cpp_full_path = os.path.join(C_CPP_SRC_DIR, cpp_file)
    h_full_path = os.path.join(C_CPP_SRC_DIR, h_file)
    if os.path.exists(cpp_full_path):
        os.remove(cpp_full_path)
        files_deleted += 1
    if os.path.exists(h_full_path):
        os.remove(h_full_path)
        files_deleted += 1
    return files_deleted


def _transpile_cpp_and_h_files(
    rel_path: str, files_added_or_modified: list[str]
) -> tuple[int, int]:
    header_files_written = 0
    cpp_files_written = 0
    if rel_path.startswith(SECRET_MAIN_FILE_DIR_PREFIX):
        # transpile a main file
        real_rel_path = rel_path[len(SECRET_MAIN_FILE_DIR_PREFIX) :]
        main_py_ast_tree: ast.Module = get_main_py_ast_tree(real_rel_path)
        main_cpp_source = calc_main_cpp_source(main_py_ast_tree)
        new_file: str = os.path.join(C_CPP_DIR, real_rel_path)[:-3] + ".cpp"
        with open(new_file, "w") as cpp_main_file:
            cpp_main_file.write(main_cpp_source)
        cpp_files_written += 1
        files_added_or_modified.append(new_file)
    else:
        # transpile src file
        # TODO: why do I do this join in here and in the get_src_py_ast_tree function?
        py_src_file = os.path.join(C_PYTHON_SRC_DIR, rel_path)
        src_file_py_ast_tree = get_src_py_ast_tree(py_src_file)
        file_without_ext = rel_path[:-3]  # Remove the .py extension
        cpp_file = file_without_ext + ".cpp"  # Remove the .py extension
        h_file = file_without_ext + ".h"
        cpp, h = calc_src_file_cpp_and_h_source(src_file_py_ast_tree, h_file)
        cpp_full_path = os.path.join(C_CPP_SRC_DIR, cpp_file)
        full_dir = os.path.dirname(cpp_full_path)
        os.makedirs(full_dir, exist_ok=True)
        if cpp != "":
            with open(cpp_full_path, "w") as cpp_write_file:
                cpp_write_file.write(cpp)
            cpp_files_written += 1
            files_added_or_modified.append(cpp_full_path)
        h_full_path = os.path.join(C_CPP_SRC_DIR, h_file)
        with open(h_full_path, "w") as h_write_file:
            h_write_file.write(h)
        header_files_written += 1
        files_added_or_modified.append(h_full_path)
    return header_files_written, cpp_files_written


def pypp_transpile() -> list[str]:
    # Step 1: Initialize the C++ project if it isn't already
    if os.path.isdir(C_CPP_DIR) and not os.path.isdir(C_CPP_BUILD_DIR):
        shutil.rmtree(C_CPP_DIR)
        print("deleted partially initialized C++ dir")
    was_initialized = initialize_cpp_project()
    if not was_initialized:
        print("C++ project directory already exists. Skipping initialization.")
    # Step 1.1 write the CmakeLists.txt file
    write_cmake_lists_file()

    # Step 2: calculate the files that have changed since the last transpile
    py_file_changes, file_timestamps = calc_py_file_changes()

    # Step 3: iterate over the deleted Py files and delete the corresponding C++ files
    files_deleted: int = 0
    for deleted_file in py_file_changes.deleted_files + py_file_changes.changed_files:
        files_deleted += _delete_cpp_and_h_file(deleted_file)

    # Step 4: iterate over the changes and now files and transpile them
    assert os.path.exists(C_PYTHON_SRC_DIR), "src/ dir must be defined; dir not found"
    os.makedirs(C_CPP_SRC_DIR, exist_ok=True)
    py_files_transpiled: int = 0
    header_files_written: int = 0
    cpp_files_written: int = 0
    files_added_or_modified: list[str] = []
    for changed_or_new_file in (
        py_file_changes.new_files + py_file_changes.changed_files
    ):
        py_files_transpiled += 1
        header_files_written, cpp_files_written = _transpile_cpp_and_h_files(
            changed_or_new_file, files_added_or_modified
        )
    print(
        f"py++ transpile finished. "
        f"files deleted: {files_deleted}, "
        f"py files transpiled: {py_files_transpiled}, "
        f"header files written: {header_files_written}, "
        f"cpp files written: {cpp_files_written}"
    )

    # Step 5: save the file timestamps
    save_timestamps(file_timestamps)

    return files_added_or_modified


if __name__ == "__main__":
    pypp_transpile()
