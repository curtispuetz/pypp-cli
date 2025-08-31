from compy_cli.src.transpilers.other.maps.maps import Maps
from compy_cli.src.transpilers.other.transpiler.util import (
    handle_imports_and_create_deps,
)
from compy_cli.src.transpilers.other.module.util.calc_includes import calc_includes
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
        py_ast: ast.Module = calc_ast(py_src_file)
        h_file: Path = file.with_suffix(".h")
        import_end, d = handle_imports_and_create_deps(
            py_ast, self._maps, self._src_py_files
        )
        cpp_code_minus_include: str = d.handle_stmts(py_ast.body[import_end:])
        h_includes, cpp_includes = calc_includes(d.ret_imports)
        cpp_code = self._calc_cpp_code(cpp_code_minus_include, h_file, cpp_includes)
        h_code: str = "#pragma once\n\n" + h_includes + " ".join(d.ret_h_file)
        return cpp_code, h_code, h_file

    def _calc_cpp_code(
        self, cpp_code_minus_include: str, h_file: Path, cpp_includes: str
    ) -> str:
        if cpp_code_minus_include.strip() != "":
            all_cpp_includes = f'#include "{h_file.as_posix()}"\n' + cpp_includes
            return all_cpp_includes + cpp_code_minus_include
        return ""

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
