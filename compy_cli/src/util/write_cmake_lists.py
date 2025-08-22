from pathlib import Path
from compy_cli.src.compy_dirs import CompyDirs


def write_cmake_lists_file(dirs: CompyDirs, main_py_files: list[Path]):
    cmake_lines = [
        "cmake_minimum_required(VERSION 4.0)",
        "project(compy LANGUAGES CXX)",
        "",
        "set(CMAKE_CXX_STANDARD 23)",
        "set(CMAKE_EXPORT_COMPILE_COMMANDS ON)",
        "",
        "file(GLOB_RECURSE SRC_FILES src/*.cpp)",
        "file(GLOB_RECURSE COMPY_FILES compy/*.cpp)",
        "file(GLOB_RECURSE LIB_FILES libs/*.cpp)",
        "",
        "add_library(compy_common STATIC ${SRC_FILES} ${COMPY_FILES} ${LIB_FILES})",
        "target_include_directories(compy_common PUBLIC "
        "${CMAKE_SOURCE_DIR}/src ${CMAKE_SOURCE_DIR}/compy ${CMAKE_SOURCE_DIR}/libs)",
        "",
    ]

    for py_file in main_py_files:
        exe_name = py_file.stem
        main_cpp = f"{exe_name}.cpp"
        cmake_lines.append(f"add_executable({exe_name} {main_cpp})")
        cmake_lines.append(f"target_link_libraries({exe_name} PRIVATE compy_common)")
        cmake_lines.append("")

    cmake_content = "\n".join(cmake_lines)

    cmake_path: Path = dirs.cpp_dir / "CMakeLists.txt"
    cmake_path.write_text(cmake_content)

    print("CMakeLists.txt generated to cpp project directory")
