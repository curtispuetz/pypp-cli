import ast
from dataclasses import dataclass
from pathlib import Path

from pypp_cli.do.transpile.transpile.handle.node import (
    create_all_transpiler_data,
)
from pypp_cli.do.transpile.transpile.z.src_files.calc_includes import (
    calc_includes,
)
from pypp_cli.do.transpile.transpile.z.src_files.handle_init_file import (
    calc_h_code_for_init_file,
)
from pypp_cli.do.transpile.transpile.calc_maps.node import Maps
from pypp_cli.do.transpile.transpile.z.results import TranspileResults


@dataclass(frozen=True, slots=True)
class SrcSingleFileTranspiler:
    _namespace: str
    _cpp_dest_dir: Path
    _py_modules: set[str]
    _lib_namespaces: dict[str, str]
    _maps: Maps
    _r: TranspileResults
    _file: Path
    _file_path: Path
    _py_ast: ast.Module

    def transpile(self):
        cpp_code, h_code, h_file = self._calc_cpp_and_h_code()
        self._write_cpp_file(cpp_code)
        self._write_h_file(h_file, h_code)

    def _calc_cpp_and_h_code(self) -> tuple[str, str, Path]:
        if self._file.stem == "__init__":
            return "", *calc_h_code_for_init_file(self._py_ast, self._file)

        h_file: Path = self._file.with_suffix(".h")
        import_end, d = create_all_transpiler_data(
            self._namespace,
            self._py_ast,
            self._maps,
            self._py_modules,
            self._lib_namespaces,
            self._file_path,
        )
        cpp_code_minus_include: str = d.handle_stmts_for_module(
            self._py_ast.body[import_end:]
        )
        h_includes, cpp_includes = calc_includes(d.cpp_includes)
        cpp_code = self._calc_cpp_code(cpp_code_minus_include, h_file, cpp_includes)
        h_code = f"#pragma once\n\n{h_includes}" + self._wrap_namespace(
            " ".join(d.ret_h_file)
        )
        return cpp_code, h_code, h_file

    def _calc_cpp_code(
        self, cpp_code_minus_include: str, h_file: Path, cpp_includes: str
    ) -> str:
        if cpp_code_minus_include.strip() != "":
            all_cpp_includes = f'#include "{h_file.as_posix()}"\n' + cpp_includes
            return all_cpp_includes + self._wrap_namespace(cpp_code_minus_include)
        return ""

    def _wrap_namespace(self, code: str) -> str:
        if self._namespace is not None:
            return f"namespace {self._namespace} {{\n{code}\n}}"
        return code

    def _write_cpp_file(self, cpp_code: str):
        cpp_file: Path = self._file.with_suffix(".cpp")
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
