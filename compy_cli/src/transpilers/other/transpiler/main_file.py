from compy_cli.src.transpilers.other.maps.maps import Maps
from compy_cli.src.transpilers.other.module.source_cltr import calc_main_cpp_source
from compy_cli.src.transpilers.other.transpiler.calc_ast_tree import calc_ast
from compy_cli.src.transpilers.other.transpiler.results import TranspileResults


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
        main_cpp_source = self._calc_cpp_source(file)
        self._write_cpp_file(file, main_cpp_source)

    def _calc_cpp_source(self, file: Path) -> str:
        py_main_file: Path = self._py_src_dir / file
        main_py_ast: ast.Module = calc_ast(py_main_file)
        return calc_main_cpp_source(main_py_ast, self._maps, self._src_py_files)

    def _write_cpp_file(self, file: Path, content: str):
        cpp_file_rel: Path = file.with_suffix(".cpp")
        cpp_file: Path = self._cpp_dest_dir / cpp_file_rel
        cpp_file.write_text(content)
        self._r.cpp_files_written += 1
        self._r.files_added_or_modified.append(cpp_file)
