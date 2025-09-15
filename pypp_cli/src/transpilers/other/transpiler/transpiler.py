import ast
from dataclasses import dataclass, field
from pathlib import Path
from pypp_cli.src.transpilers.other.other.file_tracker import PyFilesTracker
from pypp_cli.src.transpilers.other.transpiler.calc_ast_tree import calc_ast
from pypp_cli.src.transpilers.other.transpiler.maps.maps import Maps
from pypp_cli.src.transpilers.other.transpiler.main_file import (
    MainFileTranspiler,
)
from pypp_cli.src.transpilers.other.transpiler.results import TranspileResults
from pypp_cli.src.transpilers.other.transpiler.src_file import SrcFileTranspiler


@dataclass(frozen=True, slots=True)
class Transpiler:
    _src_py_files: list[Path]
    _maps: Maps
    _py_file_tracker: PyFilesTracker
    _r: TranspileResults = field(default_factory=lambda: TranspileResults([], 0, 0, 0))

    def transpile_all_changed_files(
        self,
        new_files: list[Path],
        changed_files: list[Path],
        python_dir: Path,
        cpp_dir: Path,
    ):
        main_file_transpiler = MainFileTranspiler(
            cpp_dir, self._src_py_files, self._maps, self._r
        )
        src_file_transpiler = SrcFileTranspiler(
            cpp_dir, self._src_py_files, self._maps, self._r
        )
        for file in new_files + changed_files:
            self._r.py_files_transpiled += 1
            file_path: Path = python_dir / file
            py_ast: ast.Module = calc_ast(file_path)
            assert len(py_ast.body) > 0, f"File {file_path} is empty"
            if self._is_main_block(py_ast.body[-1]):
                self._py_file_tracker.main_files.add(file)
                main_file_transpiler.transpile(file, file_path, py_ast)
            else:
                src_file_transpiler.transpile(file, file_path, py_ast)

    def get_results(self) -> TranspileResults:
        return self._r

    def _is_main_block(self, stmt: ast.stmt) -> bool:
        # TODO: put other details is this check?
        if isinstance(stmt, ast.If):
            if (
                isinstance(stmt.test, ast.Compare)
                and isinstance(stmt.test.left, ast.Name)
                and stmt.test.left.id == "__name__"
            ):
                return True
        return False
