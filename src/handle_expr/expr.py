import ast

from src.d_types import CppInclude
from src.handle_expr.h_attribute import handle_attribute
from src.handle_expr.h_bin_op import handle_bin_op
from src.handle_expr.h_call import handle_call
from src.handle_expr.h_compare import handle_compare
from src.handle_expr.h_constant import handle_constant
from src.handle_expr.h_dict import handle_dict
from src.handle_expr.h_list import handle_list
from src.handle_expr.h_name import handle_name
from src.handle_expr.h_set import handle_set
from src.handle_expr.h_subscript import handle_subscript
from src.handle_expr.h_tuple import handle_tuple
from src.handle_expr.h_unary_op import handle_unary_op
from src.handle_expr.handle_slice import handle_slice


def handle_expr(
    node: ast.expr, ret_imports: set[CppInclude], skip_cpp_lookup: bool = False
) -> str:
    if isinstance(node, ast.Compare):
        return handle_compare(node, ret_imports, handle_expr)
    if isinstance(node, ast.Name):
        return handle_name(node, ret_imports, skip_cpp_lookup)
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
    if isinstance(node, ast.Slice):
        return handle_slice(node, ret_imports, handle_expr)
    if isinstance(node, ast.BinOp):
        return handle_bin_op(node, ret_imports, handle_expr)
    if isinstance(node, ast.Tuple):
        return handle_tuple(node, ret_imports, handle_expr)
    if isinstance(node, ast.Dict):
        return handle_dict(node, ret_imports, handle_expr)
    if isinstance(node, ast.Set):
        return handle_set(node, ret_imports, handle_expr)
    raise Exception(f"code expr type {node} not handled")
