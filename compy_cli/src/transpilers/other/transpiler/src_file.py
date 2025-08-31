from compy_cli.src.transpilers.other.maps.maps import Maps
from compy_cli.src.transpilers.other.module.code_cltr import (
    calc_src_file_cpp_and_h_code,
)
from compy_cli.src.transpilers.other.transpiler.calc_ast_tree import calc_ast
from compy_cli.src.transpilers.other.transpiler.results import TranspileResults


import ast
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True, slots=True)
class SrcFileTranspiler:
    _py_src_dir: Path
    _cpp_dest_dir: Path
    _src_py_files: list[Path]
    _maps: Maps
    _r: TranspileResults

    def transpile(self, file: Path):
        cpp_code, h_code, h_file = self._calc_cpp_and_h_code(file)
        self._write_cpp_file(file, cpp_code)
        self._write_h_file(h_file, h_code)

    def _calc_cpp_and_h_code(self, file: Path) -> tuple[str, str, Path]:
        py_src_file: Path = self._py_src_dir / file
        src_file_py_ast_tree: ast.Module = calc_ast(py_src_file)
        h_file: Path = file.with_suffix(".h")
        return *calc_src_file_cpp_and_h_code(
            src_file_py_ast_tree, h_file, self._maps, self._src_py_files
        ), h_file

    def _write_cpp_file(self, file: Path, cpp_code: str):
        cpp_file: Path = file.with_suffix(".cpp")
        cpp_full_path: Path = self._cpp_dest_dir / cpp_file
        full_dir: Path = cpp_full_path.parent
        full_dir.mkdir(parents=True, exist_ok=True)
        if cpp_code != "":
            cpp_full_path.write_text(cpp_code)
            self._r.cpp_files_written += 1
            self._r.files_added_or_modified.append(cpp_full_path)

    def _write_h_file(self, h_file: Path, h_code: str):
        h_full_path: Path = self._cpp_dest_dir / h_file
        h_full_path.write_text(h_code)
        self._r.h_files_written += 1
        self._r.files_added_or_modified.append(h_full_path)
