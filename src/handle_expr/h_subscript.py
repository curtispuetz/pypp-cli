import ast

from src.handle_expr.h_tuple import handle_tuple_inner_args
from src.mapping.subscript_value import lookup_cpp_subscript_value_type
from src.util.ret_imports import RetImports


def handle_subscript(
    node: ast.Subscript,
    ret_imports: RetImports,
    handle_expr,
    include_in_header: bool,
) -> str:
    value_cpp_str = handle_expr(node.value, ret_imports, include_in_header)
    if isinstance(node.slice, ast.Tuple):
        slice_cpp_str = handle_tuple_inner_args(
            node.slice, ret_imports, handle_expr, include_in_header
        )
    else:
        slice_cpp_str: str = handle_expr(node.slice, ret_imports, include_in_header)
    v1, v2 = lookup_cpp_subscript_value_type(value_cpp_str)
    return v1 + slice_cpp_str + v2
