import ast

from src.d_types import CppInclude
from src.handle_expr.expr import handle_expr
from src.handle_stmt.h_ann_assign import handle_ann_assign
from src.handle_stmt.h_assign import handle_assign
from src.handle_stmt.h_expr import handle_stmt_expr
from src.handle_stmt.h_fn_def import handle_fn_def
from src.handle_stmt.h_if import handle_if
from src.handle_stmt.h_import_from import handle_import_from
from src.handle_stmt.h_return import handle_return


# TODO: move this to a separate file and have it have handle_stmt as a parameter?
# TODO: find places that should be using this or handle_exprs
def handle_stmts(
    stmts: list[ast.stmt], ret_imports: set[CppInclude], ret_h_file: list[str]
) -> str:
    ret: list[str] = []
    for node in stmts:
        ret.append(handle_stmt(node, ret_imports, ret_h_file))
    return " ".join(ret)


def handle_stmt(
    node: ast.stmt, ret_imports: set[CppInclude], ret_h_file: list[str]
) -> str:
    if isinstance(node, ast.FunctionDef):
        return handle_fn_def(node, ret_imports, ret_h_file, handle_stmt, handle_expr)
    if isinstance(node, ast.If):
        return handle_if(
            node, ret_imports, ret_h_file, handle_stmt, handle_stmts, handle_expr
        )
    if isinstance(node, ast.AnnAssign):
        return handle_ann_assign(node, ret_imports, handle_expr)
    if isinstance(node, ast.Return):
        return handle_return(node, ret_imports, handle_expr)
    if isinstance(node, ast.Assign):
        return handle_assign(node, ret_imports, handle_expr)
    if isinstance(node, ast.Expr):
        return handle_stmt_expr(node, ret_imports, handle_expr)
    if isinstance(node, ast.ImportFrom):
        return handle_import_from(node, ret_imports)
    raise Exception(f"code stmt type {node} not handled")
