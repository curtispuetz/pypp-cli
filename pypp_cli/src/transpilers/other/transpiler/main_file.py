from pypp_cli.src.transpilers.other.transpiler.maps.maps import Maps
from pypp_cli.src.transpilers.other.transpiler.util import (
    handle_imports_and_create_deps,
)
from pypp_cli.src.transpilers.other.transpiler.d_types import QInc
from pypp_cli.src.transpilers.other.transpiler.calc_includes import (
    calc_includes_for_main_file,
)
from pypp_cli.src.transpilers.other.transpiler.handle_main_stmts import (
    handle_main_stmts,
)
from pypp_cli.src.transpilers.other.transpiler.calc_ast_tree import calc_ast
from pypp_cli.src.transpilers.other.transpiler.results import TranspileResults


import ast
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True, slots=True)
class MainFileTranspiler:
    _py_src_dir: Path
    _cpp_dest_dir: Path
    _src_py_files: list[Path]
    _maps: Maps
    _r: TranspileResults

    def transpile(self, file: Path):
        main_cpp_code = self._calc_cpp_code(file)
        self._write_cpp_file(file, main_cpp_code)

    def _calc_cpp_code(self, file: Path) -> str:
        py_main_file: Path = self._py_src_dir / file
        py_ast: ast.Module = calc_ast(py_main_file)
        import_end, d = handle_imports_and_create_deps(
            py_ast, self._maps, self._src_py_files, py_main_file
        )
        d.add_inc(QInc("cstdlib"))
        cpp_code_minus_includes: str = handle_main_stmts(py_ast.body[import_end:], d)
        return calc_includes_for_main_file(d.cpp_includes) + cpp_code_minus_includes

    def _write_cpp_file(self, file: Path, code: str):
        cpp_file_rel: Path = file.with_suffix(".cpp")
        cpp_file: Path = self._cpp_dest_dir / cpp_file_rel
        cpp_file.write_text(code)
        self._r.cpp_files_written += 1
        self._r.files_added_or_modified.append(cpp_file)
