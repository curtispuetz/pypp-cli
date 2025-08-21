import ast
from pathlib import Path

from pypp_core.src.d_types import PyImports, PyImport, QInc
from pypp_core.src.mapping.maps.maps import Maps
from pypp_core.src.util.ret_imports import IncMap


def handle_import_stmts(
    stmts: list[ast.stmt], maps: Maps, src_py_files: list[Path]
) -> tuple[IncMap, int, PyImports]:
    modules_in_project: set[str] = _calc_all_modules_for_project(src_py_files)
    i = 0
    cpp_inc_map: IncMap = {}
    py_imports = PyImports({}, set())
    for i, node in enumerate(stmts):
        # ast.Import are ignored
        if isinstance(node, ast.ImportFrom):
            if node.module in py_imports.imp_from:
                raise Exception("Duplicate import from module not supported")
            if node.module is None:
                raise Exception("Relative imports not supported")
            if node.module in modules_in_project or maps.imports_map.contains(
                node.module
            ):
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
                if maps.imports_map.contains(name.name):
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
