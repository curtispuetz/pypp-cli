import ast
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable
from compy_cli.src.transpiler.maps.maps import Maps
from compy_cli.src.transpiler.module.source_cltr import (
    calc_main_cpp_source,
    calc_src_file_cpp_and_h_source,
)
from compy_cli.src.transpiler.util.calc_ast_tree import calc_ast_tree


@dataclass
class TranspileResults:
    files_added_or_modified: list[Path]
    py_files_transpiled: int
    header_files_written: int
    cpp_files_written: int


@dataclass(slots=True)
class Transpiler:
    _src_py_files: list[Path]
    _maps: Maps
    _files_added_or_modified: list[Path] = field(default_factory=list)
    _py_files_transpiled: int = 0
    _header_files_written: int = 0
    _cpp_files_written: int = 0

    def transpile_all_changed_files(
        self,
        new_files: list[Path],
        changed_files: list[Path],
        py_dir: Path,
        cpp_dir: Path,
        is_main_files: bool = False,
    ):
        if is_main_files:
            self._transpile_all_changed_files(
                new_files,
                changed_files,
                py_dir,
                cpp_dir,
                self._transpile_cpp_files_for_main,
            )
        else:
            self._transpile_all_changed_files(
                new_files,
                changed_files,
                py_dir,
                cpp_dir,
                self._transpile_cpp_and_h_files,
            )

    def _transpile_all_changed_files(
        self,
        new_files: list[Path],
        changed_files: list[Path],
        py_dir: Path,
        cpp_dir: Path,
        fn: Callable[[Path, Path, Path, Maps], None],
    ):
        for file in new_files + changed_files:
            self._py_files_transpiled += 1
            fn(py_dir, cpp_dir, file, self._maps)

    def _transpile_cpp_and_h_files(
        self,
        py_dir: Path,
        cpp_dir: Path,
        changed_or_new_file: Path,
        maps: Maps,
    ):
        py_src_file: Path = py_dir / changed_or_new_file
        src_file_py_ast_tree: ast.Module = calc_ast_tree(py_src_file)
        cpp_file: Path = changed_or_new_file.with_suffix(".cpp")
        h_file: Path = changed_or_new_file.with_suffix(".h")
        cpp, h = calc_src_file_cpp_and_h_source(
            src_file_py_ast_tree, h_file, maps, self._src_py_files
        )
        cpp_full_path: Path = cpp_dir / cpp_file
        full_dir: Path = cpp_full_path.parent
        full_dir.mkdir(parents=True, exist_ok=True)
        if cpp != "":
            cpp_full_path.write_text(cpp)
            self._cpp_files_written += 1
            self._files_added_or_modified.append(cpp_full_path)
        h_full_path: Path = cpp_dir / h_file
        h_full_path.write_text(h)
        self._header_files_written += 1
        self._files_added_or_modified.append(h_full_path)

    def _transpile_cpp_files_for_main(
        self,
        py_dir: Path,
        cpp_dir: Path,
        changed_or_new_file: Path,
        maps: Maps,
    ):
        py_main_file: Path = py_dir / changed_or_new_file
        main_py_ast_tree: ast.Module = calc_ast_tree(py_main_file)
        main_cpp_source: str = calc_main_cpp_source(
            main_py_ast_tree, maps, self._src_py_files
        )
        new_file_rel: Path = changed_or_new_file.with_suffix(".cpp")
        new_file: Path = cpp_dir / new_file_rel
        new_file.write_text(main_cpp_source)
        self._cpp_files_written += 1
        self._files_added_or_modified.append(Path(new_file))

    def get_results(self) -> TranspileResults:
        return TranspileResults(
            self._files_added_or_modified,
            self._py_files_transpiled,
            self._header_files_written,
            self._cpp_files_written,
        )
