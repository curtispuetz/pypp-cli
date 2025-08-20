import ast

from pypp_core.src.d_types import PyImports, PyImport
from pypp_core.src.handle_stmt.h_import_from import handle_import_from
from pypp_core.src.util.ret_imports import IncMap


def handle_import_stmts(
    stmts: list[ast.stmt], proj_info: dict
) -> tuple[IncMap, int, PyImports]:
    i = 0
    cpp_inc_map: IncMap = {}
    py_imports = PyImports({}, set())
    for i, node in enumerate(stmts):
        # ast.Import are ignored
        if isinstance(node, ast.ImportFrom):
            handle_import_from(node, proj_info, cpp_inc_map)
            if node.module in py_imports.imp_from:
                raise Exception("Duplicate import from module not supported")
            if node.module is None:
                raise Exception("Relative imports not supported")
            py_imports.imp_from[node.module] = [n.name for n in node.names]
        elif isinstance(node, ast.Import):
            for name in node.names:
                py_imports.imp.add(PyImport(name.name, name.asname))
        else:
            break
    return cpp_inc_map, i, py_imports
