import ast
from pathlib import Path

from compy_cli.src.transpilers.other.transpiler.d_types import PyImports, PyImport, QInc
from compy_cli.src.transpilers.other.transpiler.maps.maps import Maps
from compy_cli.src.transpilers.other.transpiler.cpp_includes import IncMap


def analyse_import_stmts(
    stmts: list[ast.stmt], maps: Maps, src_py_files: list[Path], file_path: Path
) -> tuple[IncMap, int, PyImports]:
    modules_in_project: set[str] = _calc_all_modules_for_project(src_py_files)
    i = 0
    cpp_inc_map: IncMap = {}
    py_imports = PyImports({}, set())
    for i, node in enumerate(stmts):
        # ast.Import are ignored
        if isinstance(node, ast.ImportFrom):
            if node.module in py_imports.imp_from:
                raise Exception(
                    f"Duplicate import from module not supported. "
                    f"module: {node.module}. In {file_path}"
                )
            if node.module is None:
                raise Exception("Relative imports not supported")
            if node.module in modules_in_project or maps.import_.contains(node.module):
                inc: QInc = _calc_q_inc(node.module)
                for alias in node.names:
                    assert alias.asname is None, "'as' is not supported in import from"
                    cpp_inc_map[alias.name] = inc
            py_imports.imp_from[node.module] = [n.name for n in node.names]
        elif isinstance(node, ast.Import):
            for name in node.names:
                if name.name in modules_in_project:
                    raise ValueError(
                        "Import is not supported for project imports "
                        "(only ImportFrom is supported)"
                    )
                if maps.import_.contains(name.name):
                    assert name.asname is not None, (
                        f"import 'as' required for {name.name}"
                    )
                    cpp_inc_map[name.asname] = _calc_q_inc(name.name)
                py_imports.imp.add(PyImport(name.name, name.asname))
        else:
            break
    return cpp_inc_map, i, py_imports


def _calc_all_modules_for_project(src_py_files: list[Path]) -> set[str]:
    ret: set[str] = set()
    for p in src_py_files:
        ret.add(p.as_posix()[:-3].replace("/", "."))
    return ret


def _calc_q_inc(name: str) -> QInc:
    return QInc(name.replace(".", "/") + ".h")
