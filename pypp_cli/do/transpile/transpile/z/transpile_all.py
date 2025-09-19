import ast
from pathlib import Path
from pypp_cli.do.transpile.find_libs.z.find_all_libs import PyppLibsData
from pypp_cli.do.transpile.y.transpiler_config_models import (
    TranspilerConfigModelsDict,
)
from pypp_cli.do.transpile.y.py_file_tracker import PyFilesTracker
from pypp_cli.do.transpile.transpile.z.calc_ast_tree import calc_ast
from pypp_cli.do.transpile.transpile.z.main_files.transpiler import (
    MainFileTranspiler,
)
from pypp_cli.do.transpile.transpile.z.src_files.transpiler import (
    SrcFileTranspiler,
)
from pypp_cli.do.transpile.transpile.z.results import TranspileResults

from pypp_cli.do.transpile.transpile.calc_maps.node import MapsCltr


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


def _calc_all_modules_for_project(py_files: list[Path]) -> set[str]:
    ret: set[str] = set()
    for p in py_files:
        if p.stem == "__init__":
            ret.add(p.parent.as_posix().replace("/", "."))
        else:
            ret.add(p.as_posix()[:-3].replace("/", "."))
    return ret


def transpile_all_changed_files(
    namespace: str,
    transpiler_config_models: TranspilerConfigModelsDict,
    libs_data: PyppLibsData,
    py_files: list[Path],
    py_files_tracker: PyFilesTracker,
    python_dir: Path,
    cpp_dir: Path,
    new_files: list[Path],
    changed_files: list[Path],
) -> TranspileResults:
    maps_cltr = MapsCltr(transpiler_config_models)
    maps = maps_cltr.calc_maps()
    py_modules = _calc_all_modules_for_project(py_files)
    ret: TranspileResults = TranspileResults([], 0, 0, 0)
    main_file_transpiler = MainFileTranspiler(
        namespace, cpp_dir, py_modules, libs_data.namespaces, maps, ret
    )
    src_file_transpiler = SrcFileTranspiler(
        namespace, cpp_dir, py_modules, libs_data.namespaces, maps, ret
    )

    for file in new_files + changed_files:
        ret.py_files_transpiled += 1
        file_path: Path = python_dir / file
        py_ast: ast.Module = calc_ast(file_path)
        if _is_proper_main_block(py_ast.body[-1]):
            py_files_tracker.main_files.add(file)
            main_file_transpiler.transpile(file, file_path, py_ast)
        else:
            src_file_transpiler.transpile(file, file_path, py_ast)
    return ret
