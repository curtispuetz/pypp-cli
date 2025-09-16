import ast
from dataclasses import dataclass
from pathlib import Path
from pypp_cli.src.transpilers.library.file_tracker import PyFilesTracker
from .util.calc_ast_tree import calc_ast
from .maps.maps import Maps
from pypp_cli.src.transpilers.library.transpiler.files.main.main_file import (
    MainFileTranspiler,
)
from pypp_cli.src.transpilers.library.transpiler.files.src.src_file import (
    SrcFileTranspiler,
)
from .util.results import TranspileResults


def _is_proper_main_block(node: ast.stmt) -> bool:
    if not isinstance(node, ast.If):
        return False
    if len(node.orelse) != 0:
        return False
    if not isinstance(node.test, ast.Compare):
        return False
    if not isinstance(node.test.left, ast.Name):
        return False
    if node.test.left.id != "__name__":
        return False
    if len(node.test.ops) != 1:
        return False
    if not isinstance(node.test.ops[0], ast.Eq):
        return False
    if len(node.test.comparators) != 1:
        return False
    comp = node.test.comparators[0]
    if not isinstance(comp, ast.Constant):
        return False
    if comp.value != "__main__":
        return False
    return True


@dataclass(frozen=True, slots=True)
class Transpiler:
    _py_files: list[Path]
    _maps: Maps
    _py_file_tracker: PyFilesTracker

    def transpile_all_changed_files(
        self,
        new_files: list[Path],
        changed_files: list[Path],
        python_dir: Path,
        cpp_dir: Path,
    ) -> TranspileResults:
        ret: TranspileResults = TranspileResults([], 0, 0, 0)
        main_file_transpiler = MainFileTranspiler(
            cpp_dir, self._py_files, self._maps, ret
        )
        src_file_transpiler = SrcFileTranspiler(
            cpp_dir, self._py_files, self._maps, ret
        )
        for file in new_files + changed_files:
            ret.py_files_transpiled += 1
            file_path: Path = python_dir / file
            py_ast: ast.Module = calc_ast(file_path)
            assert len(py_ast.body) > 0, f"File {file_path} is empty"
            if _is_proper_main_block(py_ast.body[-1]):
                self._py_file_tracker.main_files.add(file)
                main_file_transpiler.transpile(file, file_path, py_ast)
            else:
                src_file_transpiler.transpile(file, file_path, py_ast)
        return ret
