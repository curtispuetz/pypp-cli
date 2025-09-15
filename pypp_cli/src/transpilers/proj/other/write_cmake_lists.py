from ast import main
from dataclasses import dataclass
import json
from pathlib import Path

from pypp_cli.src.transpilers.other.other.bridge_json_path_cltr import (
    BridgeJsonPathCltr,
)
from pypp_cli.src.transpilers.other.other.file_tracker import PyFilesTracker


def _calc_link_libs_lines(link_libs: list[str]) -> list[str]:
    # target_link_libraries(pypp_common PUBLIC glfw)
    if len(link_libs) == 0:
        return []
    return [
        "target_link_libraries(",
        "    pypp_common PUBLIC",
        *[f"    {lib}" for lib in link_libs],
        ")",
    ]


@dataclass(frozen=True, slots=True)
class CMakeListsWriter:
    _cpp_dir: Path
    _bridge_json_path_cltr: BridgeJsonPathCltr
    _bridge_libs: list[str]
    _cmake_minimum_required_version: str
    _py_files_tracker: PyFilesTracker

    def write(self):
        main_files, src_files = self._calc_main_and_src_files()
        add_lines, link_libs = self._calc_add_lines_and_link_libs_from_libraries()
        cmake_lines = [
            f"cmake_minimum_required(VERSION {self._cmake_minimum_required_version})",
            "set(CMAKE_CXX_COMPILER clang++)",
            "set(CMAKE_C_COMPILER clang)",
            "project(pypp LANGUAGES C CXX)",
            "",
            "set(CMAKE_CXX_STANDARD 23)",
            "set(CMAKE_EXPORT_COMPILE_COMMANDS ON)",
            "",
            *add_lines,
            "",
            "set(SRC_FILES",
            *src_files,
            ")",
            "file(GLOB_RECURSE pypp_FILES pypp/*.cpp)",
            "file(GLOB_RECURSE LIB_FILES libs/*.cpp)",
            "",
            "add_library(",
            "    pypp_common STATIC",
            "    ${SRC_FILES}",
            "    ${pypp_FILES}",
            "    ${LIB_FILES}",
            ")",
            "target_include_directories(",
            "    pypp_common PUBLIC",
            "    ${CMAKE_SOURCE_DIR}",
            "    ${CMAKE_SOURCE_DIR}/pypp",
            "    ${CMAKE_SOURCE_DIR}/libs",
            ")",
            *_calc_link_libs_lines(link_libs),
            "",
        ]

        for py_file in main_files:
            exe_name = py_file.stem
            cmake_lines.append(f"add_executable({exe_name} {exe_name}.cpp)")
            cmake_lines.append(f"target_link_libraries({exe_name} PRIVATE pypp_common)")
            cmake_lines.append("")

        cmake_content = "\n".join(cmake_lines)

        cmake_path: Path = self._cpp_dir / "CMakeLists.txt"
        cmake_path.write_text(cmake_content)

        print("CMakeLists.txt generated to cpp project directory")

    def _calc_main_and_src_files(self) -> tuple[list[Path], list[str]]:
        main_files: list[Path] = []
        src_files: list[str] = []
        for f in self._py_files_tracker.all_files:
            if f.name == "__init__.py":
                continue
            if f in self._py_files_tracker.main_files:
                main_files.append(f)
            else:
                # replace stem with cpp
                cpp_file: Path = f.with_suffix(".cpp")
                if (self._cpp_dir / cpp_file).exists():
                    src_files.append(cpp_file.as_posix())
        return main_files, src_files

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
