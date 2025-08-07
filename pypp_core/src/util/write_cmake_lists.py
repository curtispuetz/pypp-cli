import os

from pypp_core.src.config import C_PYTHON_DIR, C_CPP_DIR
from pypp_core.src.util.file_change_tracker import get_all_main_files


def write_cmake_lists_file():
    # Find all .py files in the directory
    main_py_files = get_all_main_files()
    if not main_py_files:
        raise Exception(f"No Python files (*.py) found in '{C_PYTHON_DIR}'.")

    cmake_lines = [
        "cmake_minimum_required(VERSION 4.0)",
        "project(pypp LANGUAGES CXX)",
        "",
        "set(CMAKE_CXX_STANDARD 23)",
        "set(CMAKE_EXPORT_COMPILE_COMMANDS ON)",
        "",
        "file(GLOB_RECURSE SRC_FILES src/*.cpp)",
        "file(GLOB_RECURSE PYPP_FILES pypp/*.cpp)",
        "",
        "add_library(pypp_common STATIC ${SRC_FILES} ${PYPP_FILES})",
        "target_include_directories(pypp_common PUBLIC ${CMAKE_SOURCE_DIR}/src ${CMAKE_SOURCE_DIR}/pypp)",
        "",
    ]

    for py_file in main_py_files:
        exe_name = os.path.splitext(py_file)[0]
        main_cpp = f"{exe_name}.cpp"
        cmake_lines.append(f"add_executable({exe_name} {main_cpp})")
        cmake_lines.append(f"target_link_libraries({exe_name} PRIVATE pypp_common)")
        cmake_lines.append("")

    cmake_content = "\n".join(cmake_lines)

    cmake_path = os.path.join(C_CPP_DIR, "CMakeLists.txt")
    with open(cmake_path, "w", encoding="utf-8") as f:
        f.write(cmake_content)

    print(f"CMakeLists.txt generated successfully at {cmake_path}")
