import ast
import os
import shutil

from src.config import (
    C_PYTHON_SRC_DIR,
    C_CPP_MAIN_FILE,
    C_CPP_DIR,
    C_CPP_BUILD_DIR,
    C_CPP_SRC_DIR,
)
from src.constants import MAIN_FILE_SECRET_NAME
from src.util.file_change_tracker import (
    PyFileChanges,
    calc_py_file_changes,
)
from src.util.initalize_cpp import initialize_cpp_project
from src.util.get_py import get_main_py_ast_tree, get_src_py_ast_tree
from src.util.main_source import calc_main_cpp_source, calc_src_file_cpp_and_h_source


def pypp_transpile() -> list[str]:
    # Step 1: Initialize the C++ project if it isn't already
    if os.path.isdir(C_CPP_DIR) and not os.path.isdir(C_CPP_BUILD_DIR):
        shutil.rmtree(C_CPP_DIR)
        print("deleted partially initialized C++ dir")
    was_initialized = initialize_cpp_project()
    if not was_initialized:
        print("C++ project directory already exists. Skipping initialization.")

    # Step 2: calculate the files that have changed since the last transpile
    py_file_changes: PyFileChanges = calc_py_file_changes()

    # Step 3: iterate over the deleted Py files and delete the corresponding C++ files
    files_deleted: int = 0
    for deleted_file in py_file_changes.deleted_files:
        if deleted_file == MAIN_FILE_SECRET_NAME:
            raise Exception("main.py file was deleted; cannot delete the main.py file")
        deleted_file_without_ext = deleted_file[:-3]  # Remove the .py extension
        cpp_file = deleted_file_without_ext + ".cpp"
        h_file = deleted_file_without_ext + ".h"
        cpp_full_path = os.path.join(C_CPP_SRC_DIR, cpp_file)
        h_full_path = os.path.join(C_CPP_SRC_DIR, h_file)
        if os.path.exists(cpp_full_path):
            os.remove(cpp_full_path)
            files_deleted += 1
        if os.path.exists(h_full_path):
            os.remove(h_full_path)
            files_deleted += 1

    # Step 4: iterate over the changes and now files and transpile them
    assert os.path.exists(C_PYTHON_SRC_DIR), "src/ dir must be defined; dir not found"
    os.makedirs(C_CPP_SRC_DIR, exist_ok=True)
    py_files_transpiled: int = 0
    header_files_written: int = 0
    cpp_files_written: int = 0
    files_added_or_modified: list[str] = []
    for changed_or_new_file in py_file_changes.changed_or_new_files:
        py_files_transpiled += 1
        if changed_or_new_file == MAIN_FILE_SECRET_NAME:
            # Transpile the main.py file
            main_py_ast_tree: ast.Module = get_main_py_ast_tree()
            main_cpp_source = calc_main_cpp_source(main_py_ast_tree)
            with open(C_CPP_MAIN_FILE, "w") as cpp_main_file:
                cpp_main_file.write(main_cpp_source)
            print("Wrote main.cpp")
            cpp_files_written += 1
            files_added_or_modified.append(C_CPP_MAIN_FILE)
        else:
            # transpile src file
            py_src_file = os.path.join(C_PYTHON_SRC_DIR, changed_or_new_file)
            src_file_py_ast_tree = get_src_py_ast_tree(py_src_file)
            file_without_ext = changed_or_new_file[:-3]  # Remove the .py extension
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
    print(
        f"py++ transpile finished. "
        f"files deleted: {files_deleted}, "
        f"py files transpiled: {py_files_transpiled}, "
        f"header files written: {header_files_written}, "
        f"cpp files written: {cpp_files_written}"
    )
    return files_added_or_modified


if __name__ == "__main__":
    pypp_transpile()
