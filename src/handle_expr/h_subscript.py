import ast

from src.d_types import CppInclude
from src.mapping.subscript_value import lookup_cpp_subscript_value_type


def handle_subscript(
    node: ast.Subscript, ret_imports: set[CppInclude], handle_expr
) -> str:
    value_cpp_str = handle_expr(node.value, ret_imports)
    slice_cpp_str = handle_expr(node.slice, ret_imports)
    v1, v2 = lookup_cpp_subscript_value_type(value_cpp_str)
    return v1 + slice_cpp_str + v2
