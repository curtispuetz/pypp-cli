import ast

from src.d_types import CppInclude


# TODO: find places that should be using this or handle_exprs
def handle_stmts(
    stmts: list[ast.stmt],
    ret_imports: set[CppInclude],
    ret_h_file: list[str],
    handle_stmt,
) -> str:
    ret: list[str] = []
    for node in stmts:
        ret.append(handle_stmt(node, ret_imports, ret_h_file))
    return " ".join(ret)


def handle_exprs(
    exprs: list[ast.expr], ret_imports: set[CppInclude], handle_expr
) -> str:
    ret: list[str] = []
    for node in exprs:
        ret.append(handle_expr(node, ret_imports))
    return ", ".join(ret)  # Note: is it always going to join like this?
