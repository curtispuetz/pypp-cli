from dataclasses import dataclass
import json
from pathlib import Path

from compy_cli.src.bridge_json_path_cltr import BridgeJsonPathCltr


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


@dataclass(frozen=True, slots=True)
class CMakeListsWriter:
    _cpp_dir: Path
    _bridge_json_path_cltr: BridgeJsonPathCltr
    _main_py_files: list[Path]
    _bridge_libs: list[str]

    def write(self, ignored_main_file_stems: set[str]):
        add_lines, link_libs = self._calc_add_lines_and_link_libs_from_libraries()
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

        for py_file in self._main_py_files:
            exe_name = py_file.stem
            main_cpp = f"{exe_name}.cpp"
            if exe_name not in ignored_main_file_stems:
                cmake_lines.append(f"add_executable({exe_name} {main_cpp})")
                cmake_lines.append(
                    f"target_link_libraries({exe_name} PRIVATE compy_common)"
                )
                cmake_lines.append("")

        cmake_content = "\n".join(cmake_lines)

        cmake_path: Path = self._cpp_dir / "CMakeLists.txt"
        cmake_path.write_text(cmake_content)

        print("CMakeLists.txt generated to cpp project directory")

    def _calc_add_lines_and_link_libs_from_libraries(
        self,
    ) -> tuple[list[str], list[str]]:
        add_lines: list[str] = []
        link_libs: list[str] = []
        for bridge_lib in self._bridge_libs:
            cmake_lists: Path = self._bridge_json_path_cltr.calc_bridge_json(
                bridge_lib, "cmake_lists"
            )
            if cmake_lists.exists():
                with open(cmake_lists, "r") as f:
                    data = json.load(f)
                # Note: the json should be validated already when the library is
                # installed.
                # TODO later: instead of just assuming the structure is correct,
                #  I could now
                #  easily just call the validation functions I have even though it
                #  should
                #  rarely be nessesary. Because it would be more safe and should be
                #  super fast anyway.
                add_lines.extend(data["add_lines"])
                link_libs.extend(data["link_libraries"])
        return add_lines, link_libs
