import ast

from src.handle_stmt.h_import_from import handle_import_from
from src.util.ret_imports import RetImports, ImpMap


def handle_import_stmts(stmts: list[ast.stmt]) -> tuple[ImpMap, int]:
    assert len(stmts) > 0, "Empty files not supported"
    ret: ImpMap = {}
    for i, node in enumerate(stmts):
        # ast.Import are ignored
        if isinstance(node, ast.ImportFrom):
            handle_import_from(node, ret)
        elif not isinstance(node, ast.Import):
            break
    return ret, i


def handle_stmts(
    stmts: list[ast.stmt],
    ret_imports: RetImports,
    ret_h_file: list[str],
    handle_stmt,
) -> str:
    ret: list[str] = []
    for node in stmts:
        ret.append(handle_stmt(node, ret_imports, ret_h_file))
    return " ".join(ret)


def handle_exprs(
    exprs: list[ast.expr],
    ret_imports: RetImports,
    handle_expr,
    include_in_header: bool = False,
) -> str:
    ret: list[str] = []
    for node in exprs:
        ret.append(handle_expr(node, ret_imports, include_in_header))
    return ", ".join(ret)  # Note: is it always going to join like this?
