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
from src.util.initalize_cpp import initialize_cpp_project
from src.util.calc_src_files import calc_py_src_files
from src.util.delete_cpp_files import delete_cpp_main_and_src_dir
from src.util.get_py import get_main_py_ast_tree, get_src_py_ast_tree
from src.util.main_source import calc_main_cpp_source, calc_src_file_cpp_and_h_source


def pypp_transpile():
    if os.path.isdir(C_CPP_DIR) and not os.path.isdir(C_CPP_BUILD_DIR):
        shutil.rmtree(C_CPP_DIR)
        print("deleted partially initialized C++ dir")
    was_initialized = initialize_cpp_project()
    if not was_initialized:
        print("C++ project directory already exists. Skipping initialization.")
    delete_cpp_main_and_src_dir()

    # Step 1: transpile the main.py file
    # Step 1.1: get the main file string
    main_py_ast_tree: ast.Module = get_main_py_ast_tree()
    main_cpp_source = calc_main_cpp_source(main_py_ast_tree)
    # Step 1.2: write the string to a main.cpp file
    with open(C_CPP_MAIN_FILE, "x") as cpp_main_file:
        cpp_main_file.write(main_cpp_source)
    print("Wrote main.cpp")

    # Step 3: transpile the src/ dir
    assert os.path.exists(C_PYTHON_SRC_DIR), "src/ dir must be defined; dir not found"
    os.makedirs(C_CPP_SRC_DIR, exist_ok=False)
    for py_src_file in calc_py_src_files():
        src_file_py_ast_tree = get_src_py_ast_tree(py_src_file)
        cpp_file = py_src_file.with_suffix(".cpp")
        h_file = py_src_file.with_suffix(".h")
        cpp, h = calc_src_file_cpp_and_h_source(src_file_py_ast_tree, h_file)
        with open(os.path.join(C_CPP_SRC_DIR, cpp_file), "x") as cpp_write_file:
            cpp_write_file.write(cpp)
        with open(os.path.join(C_CPP_SRC_DIR, h_file), "x") as h_write_file:
            h_write_file.write(h)
    print("Wrote C++ src files")
    print("py++ transpile finished")


if __name__ == "__main__":
    pypp_transpile()
