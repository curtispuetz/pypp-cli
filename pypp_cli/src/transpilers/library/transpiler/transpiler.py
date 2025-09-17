import ast
from pathlib import Path
from pypp_cli.src.transpilers.library.bridge_libs.finder import PyppLibs
from pypp_cli.src.transpilers.library.file_tracker import PyFilesTracker
from .util.calc_ast_tree import calc_ast
from pypp_cli.src.transpilers.library.transpiler.files.main.main_file import (
    MainFileTranspiler,
)
from pypp_cli.src.transpilers.library.transpiler.files.src.src_file import (
    SrcFileTranspiler,
)
from .util.results import TranspileResults


from pypp_cli.src.transpilers.library.bridge_libs.path_cltr import (
    BridgeJsonPathCltr,
)
from pypp_cli.src.transpilers.library.transpiler.maps.maps import MapsCltr
from pypp_cli.src.transpilers.library.transpiler.maps.util.calc_import_map import (
    ImportMapCltr,
)
from pypp_cli.src.transpilers.library.transpiler.maps.util.calc_map_1 import MapCltr1
from pypp_cli.src.transpilers.library.transpiler.maps.util.calc_map_2 import MapCltr2


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
    bridge_json_path_cltr: BridgeJsonPathCltr,
    libs: PyppLibs,
    py_files: list[Path],
    py_files_tracker: PyFilesTracker,
    python_dir: Path,
    cpp_dir: Path,
    new_files: list[Path],
    changed_files: list[Path],
) -> TranspileResults:
    maps_cltr = MapsCltr(
        MapCltr1(libs, bridge_json_path_cltr),
        MapCltr2(libs, bridge_json_path_cltr),
        ImportMapCltr(libs, bridge_json_path_cltr),
    )
    maps = maps_cltr.calc_maps()
    py_modules = _calc_all_modules_for_project(py_files)
    ret: TranspileResults = TranspileResults([], 0, 0, 0)
    main_file_transpiler = MainFileTranspiler(cpp_dir, py_modules, maps, ret)
    src_file_transpiler = SrcFileTranspiler(cpp_dir, py_modules, maps, ret)

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
