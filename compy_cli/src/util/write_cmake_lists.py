import json
from pathlib import Path
from compy_cli.src.util.create_all_data import WriteCmakeListsFileDeps


def write_cmake_lists_file(
    d: WriteCmakeListsFileDeps,
    ignored_main_file_stems: set[str],
):
    add_lines, link_libs = _calc_add_lines_and_link_libs_from_libraries(d)
    cmake_lines = [
        "cmake_minimum_required(VERSION 4.0)",
        "project(compy LANGUAGES CXX)",
        "",
        "set(CMAKE_CXX_STANDARD 23)",
        "set(CMAKE_EXPORT_COMPILE_COMMANDS ON)",
        "",
        *add_lines,
        "",
        "file(GLOB_RECURSE SRC_FILES src/*.cpp)",
        "file(GLOB_RECURSE COMPY_FILES compy/*.cpp)",
        "file(GLOB_RECURSE LIB_FILES libs/*.cpp)",
        "",
        "add_library(",
        "    compy_common STATIC",
        "    ${SRC_FILES}",
        "    ${COMPY_FILES}",
        "    ${LIB_FILES}",
        ")",
        "target_include_directories(",
        "    compy_common PUBLIC",
        "    ${CMAKE_SOURCE_DIR}/src",
        "    ${CMAKE_SOURCE_DIR}/compy",
        "    ${CMAKE_SOURCE_DIR}/libs",
        ")",
        *_calc_link_libs_lines(link_libs),
        "",
    ]

    for py_file in d.main_py_files:
        exe_name = py_file.stem
        main_cpp = f"{exe_name}.cpp"
        if exe_name not in ignored_main_file_stems:
            cmake_lines.append(f"add_executable({exe_name} {main_cpp})")
            cmake_lines.append(
                f"target_link_libraries({exe_name} PRIVATE compy_common)"
            )
            cmake_lines.append("")

    cmake_content = "\n".join(cmake_lines)

    cmake_path: Path = d.dirs.cpp_dir / "CMakeLists.txt"
    cmake_path.write_text(cmake_content)

    print("CMakeLists.txt generated to cpp project directory")


def _calc_add_lines_and_link_libs_from_libraries(
    d: WriteCmakeListsFileDeps,
) -> tuple[list[str], list[str]]:
    add_lines: list[str] = []
    link_libs: list[str] = []
    for installed_library in d.proj_info.installed_bridge_libs:
        cmake_lists: Path = d.dirs.calc_bridge_json(installed_library, "cmake_lists")
        if cmake_lists.exists():
            with open(cmake_lists, "r") as f:
                data = json.load(f)
            # Note: the json should be validated already when the library is installed.
            # TODO later: instead of just assuming the structure is correct, I could now
            #  easily just call the validation functions I have even though it should
            #  rarely be nessesary. Because it would be more safe and should be
            #  super fast anyway.
            add_lines.extend(data["add_lines"])
            link_libs.extend(data["link_libraries"])
    return add_lines, link_libs


def _calc_link_libs_lines(link_libs: list[str]) -> list[str]:
    # target_link_libraries(compy_common PUBLIC glfw)
    if len(link_libs) == 0:
        return []
    return [
        "target_link_libraries(",
        "    compy_common PUBLIC",
        *[f"    {lib}" for lib in link_libs],
        ")",
    ]
