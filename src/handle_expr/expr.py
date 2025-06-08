import ast

from src.d_types import CppInclude
from src.handle_expr.h_attribute import handle_attribute
from src.handle_expr.h_call import handle_call
from src.handle_expr.h_compare import handle_compare
from src.handle_expr.h_constant import handle_constant
from src.handle_expr.h_list import handle_list
from src.handle_expr.h_name import handle_name
from src.handle_expr.h_subscript import handle_subscript
from src.handle_expr.h_unary_op import handle_unary_op


def handle_expr(node: ast.expr, ret_imports: set[CppInclude]) -> str:
    if isinstance(node, ast.Compare):
        return handle_compare(node, ret_imports, handle_expr)
    if isinstance(node, ast.Name):
        return handle_name(node)
    if isinstance(node, ast.Constant):
        return handle_constant(node, ret_imports)
    if isinstance(node, ast.Call):
        return handle_call(node, ret_imports, handle_expr)
    if isinstance(node, ast.Subscript):
        return handle_subscript(node, ret_imports, handle_expr)
    if isinstance(node, ast.List):
        return handle_list(node, ret_imports, handle_expr)
    if isinstance(node, ast.Attribute):
        return handle_attribute(node, ret_imports, handle_expr)
    if isinstance(node, ast.UnaryOp):
        return handle_unary_op(node, ret_imports, handle_expr)
    raise Exception(f"code expr type {node} not handled")
