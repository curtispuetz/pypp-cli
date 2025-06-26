import ast

from src.handle_expr.h_attribute import handle_attribute
from src.handle_expr.h_bin_op import handle_bin_op
from src.handle_expr.h_call import handle_call
from src.handle_expr.h_compare import handle_compare
from src.handle_expr.h_constant import handle_constant
from src.handle_expr.h_dict import handle_dict
from src.handle_expr.h_joined_string import handle_joined_string
from src.handle_expr.h_list import handle_list
from src.handle_expr.h_name import handle_name
from src.handle_expr.h_set import handle_set
from src.handle_expr.h_subscript import handle_subscript
from src.handle_expr.h_tuple import handle_tuple
from src.handle_expr.h_unary_op import handle_unary_op
from src.handle_expr.h_slice import handle_slice
from src.util.ret_imports import RetImports


def handle_expr(
    node: ast.expr,
    ret_imports: RetImports,
    include_in_header: bool = False,
    skip_cpp_lookup: bool = False,
) -> str:
    if isinstance(node, ast.Compare):
        return handle_compare(node, ret_imports, handle_expr, include_in_header)
    if isinstance(node, ast.Name):
        return handle_name(node, ret_imports, skip_cpp_lookup, include_in_header)
    if isinstance(node, ast.Constant):
        return handle_constant(node, ret_imports, include_in_header)
    if isinstance(node, ast.Call):
        return handle_call(node, ret_imports, handle_expr, include_in_header)
    if isinstance(node, ast.Subscript):
        return handle_subscript(node, ret_imports, handle_expr, include_in_header)
    if isinstance(node, ast.List):
        return handle_list(node, ret_imports, handle_expr, include_in_header)
    if isinstance(node, ast.Attribute):
        return handle_attribute(node, ret_imports, handle_expr, include_in_header)
    if isinstance(node, ast.UnaryOp):
        return handle_unary_op(node, ret_imports, handle_expr, include_in_header)
    if isinstance(node, ast.Slice):
        return handle_slice(node, ret_imports, handle_expr, include_in_header)
    if isinstance(node, ast.BinOp):
        return handle_bin_op(node, ret_imports, handle_expr, include_in_header)
    if isinstance(node, ast.Tuple):
        return handle_tuple(node, ret_imports, handle_expr, include_in_header)
    if isinstance(node, ast.Dict):
        return handle_dict(node, ret_imports, handle_expr, include_in_header)
    if isinstance(node, ast.Set):
        return handle_set(node, ret_imports, handle_expr, include_in_header)
    if isinstance(node, ast.JoinedStr):
        return handle_joined_string(node, ret_imports, handle_expr, include_in_header)
    if isinstance(node, (ast.ListComp, ast.SetComp, ast.DictComp)):
        raise Exception("Shouldn't happen. This should be called from ann_assign")
    if isinstance(node, ast.GeneratorExp):
        raise Exception("Generator expressions are not supported")
    raise Exception(f"code expr type {node} not handled")
