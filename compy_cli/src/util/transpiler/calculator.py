import ast
from dataclasses import dataclass
from pathlib import Path
from typing import Callable
from compy_cli.src.mapping.maps.maps import Maps, calc_maps
from compy_cli.src.util.calc_ast_tree import calc_ast_tree
from compy_cli.src.util.transpiler.create_all_data import TranspileDeps
from compy_cli.src.util.source_calculator import (
    calc_main_cpp_source,
    calc_src_file_cpp_and_h_source,
)


@dataclass
class TranspileResults:
    files_added_or_modified: list[Path]
    py_files_transpiled: int
    header_files_written: int
    cpp_files_written: int


def transpile_all_changed_files(
    d: TranspileDeps,
    new_files: list[Path],
    changed_files: list[Path],
    is_main_files: bool = False,
) -> TranspileResults:
    transpiler = _Transpiler(d, is_main_files)
    transpiler.transpile_all_changed_files(new_files, changed_files)
    return TranspileResults(
        transpiler.files_added_or_modified,
        transpiler.py_files_transpiled,
        transpiler.header_files_written,
        transpiler.cpp_files_written,
    )


class _Transpiler:
    def __init__(
        self,
        d: TranspileDeps,
        is_main_files: bool = False,
    ) -> None:
        self._d = d
        self.files_added_or_modified: list[Path] = []
        self.py_files_transpiled: int = 0
        self.header_files_written: int = 0
        self.cpp_files_written: int = 0
        self._is_main_files = is_main_files

    def transpile_all_changed_files(
        self, new_files: list[Path], changed_files: list[Path]
    ):
        if self._is_main_files:
            self._transpile_all_changed_files(
                new_files,
                changed_files,
                self._transpile_cpp_files_for_main,
            )
        else:
            self._transpile_all_changed_files(
                new_files,
                changed_files,
                self._transpile_cpp_and_h_files,
            )

    def _transpile_all_changed_files(
        self,
        new_files: list[Path],
        changed_files: list[Path],
        fn: Callable[[Path, Maps], None],
    ):
        maps: Maps | None = None
        for file in new_files + changed_files:
            self.py_files_transpiled += 1
            if maps is None:
                maps = calc_maps(self._d.proj_info, self._d.dirs)
            fn(file, maps)

    def _transpile_cpp_and_h_files(
        self,
        changed_or_new_file: Path,
        maps: Maps,
    ):
        py_src_file: Path = self._d.dirs.python_src_dir / changed_or_new_file
        src_file_py_ast_tree: ast.Module = calc_ast_tree(py_src_file)
        cpp_file: Path = changed_or_new_file.with_suffix(".cpp")
        h_file: Path = changed_or_new_file.with_suffix(".h")
        cpp, h = calc_src_file_cpp_and_h_source(
            src_file_py_ast_tree, h_file, maps, self._d.src_py_files
        )
        cpp_full_path: Path = self._d.dirs.cpp_src_dir / cpp_file
        full_dir: Path = cpp_full_path.parent
        full_dir.mkdir(parents=True, exist_ok=True)
        if cpp != "":
            cpp_full_path.write_text(cpp)
            self.cpp_files_written += 1
            self.files_added_or_modified.append(cpp_full_path)
        h_full_path: Path = self._d.dirs.cpp_src_dir / h_file
        h_full_path.write_text(h)
        self.header_files_written += 1
        self.files_added_or_modified.append(h_full_path)

    def _transpile_cpp_files_for_main(
        self,
        changed_or_new_file: Path,
        maps: Maps,
    ):
        py_main_file: Path = self._d.dirs.python_dir / changed_or_new_file
        main_py_ast_tree: ast.Module = calc_ast_tree(py_main_file)
        main_cpp_source: str = calc_main_cpp_source(
            main_py_ast_tree, maps, self._d.src_py_files
        )
        new_file_rel: Path = changed_or_new_file.with_suffix(".cpp")
        new_file: Path = self._d.dirs.cpp_dir / new_file_rel
        new_file.write_text(main_cpp_source)
        self.cpp_files_written += 1
        self.files_added_or_modified.append(Path(new_file))
