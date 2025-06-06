import ast

from src.d_types import CppInclude
from src.handle_expr.h_call import handle_call
from src.handle_expr.h_compare import handle_compare
from src.handle_expr.h_constant import handle_constant
from src.handle_expr.h_name import handle_name


def handle_exprs(exprs: list[ast.expr], ret_imports: set[CppInclude]) -> str:
    ret: list[str] = []
    for node in exprs:
        ret.append(handle_expr(node, ret_imports))
    return ", ".join(ret)  # Note: is it always going to join like this?


def handle_expr(node: ast.expr, ret_imports: set[CppInclude]) -> str:
    if isinstance(node, ast.Compare):
        return handle_compare(node, ret_imports, handle_expr)
    if isinstance(node, ast.Name):
        return handle_name(node)
    if isinstance(node, ast.Constant):
        return handle_constant(node)
    if isinstance(node, ast.Call):
        return handle_call(node, ret_imports, handle_expr, handle_exprs)
    raise Exception(f"code expr type {node} not handled")
