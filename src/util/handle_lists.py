import ast

from src.deps import Deps
from src.handle_stmt.h_import_from import handle_import_from
from src.util.ret_imports import ImpMap


def handle_import_stmts(stmts: list[ast.stmt]) -> tuple[ImpMap, int]:
    i = 0
    ret: ImpMap = {}
    for i, node in enumerate(stmts):
        # ast.Import are ignored
        if isinstance(node, ast.ImportFrom):
            handle_import_from(node, ret)
        elif not isinstance(node, ast.Import):
            break
    return ret, i


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
