import ast

from pypp_core.src.d_types import PyImports, PyImport
from pypp_core.src.deps import Deps
from pypp_core.src.handle_stmt.h_import_from import handle_import_from
from pypp_core.src.util.ret_imports import ImpMap


def handle_import_stmts(
    stmts: list[ast.stmt], proj_info: dict
) -> tuple[ImpMap, int, PyImports]:
    i = 0
    cpp_imp_map: ImpMap = {}
    py_imports = PyImports({}, set())
    for i, node in enumerate(stmts):
        # ast.Import are ignored
        if isinstance(node, ast.ImportFrom):
            handle_import_from(node, proj_info, cpp_imp_map)
            if node.module in py_imports.imp_from:
                raise Exception("Duplicate import from module not supported")
            if node.module is None:
                raise Exception("Relative imports not supported")
            # Note: the str call is unnecessary, but the type checker is having an issue
            #  without it.
            py_imports.imp_from[node.module] = [str(n.name) for n in node.names]
        elif isinstance(node, ast.Import):
            for name in node.names:
                py_imports.imp.add(PyImport(name.name, name.asname))
        else:
            break
    return cpp_imp_map, i, py_imports


def handle_stmts(stmts: list[ast.stmt], d: Deps) -> str:
    ret: list[str] = []
    for node in stmts:
        ret.append(d.handle_stmt(node, d))
    return " ".join(ret)


def handle_exprs(
    exprs: list[ast.expr],
    d: Deps,
    include_in_header: bool = False,
) -> str:
    ret: list[str] = []
    for node in exprs:
        ret.append(d.handle_expr(node, include_in_header))
    return ", ".join(ret)  # Note: is it always going to join like this?
