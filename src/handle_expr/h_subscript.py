import ast

from src.d_types import CppInclude
from src.mapping.types import lookup_cpp_type, lookup_cpp_subscript_value_type


def handle_subscript(
    node: ast.Subscript, ret_imports: set[CppInclude], handle_expr
) -> str:
    value_py_str = handle_expr(node.value, ret_imports)
    slice_py_str = handle_expr(node.slice, ret_imports)
    # Now I need to lookup the cpp types
    v1, v2 = lookup_cpp_subscript_value_type(value_py_str, ret_imports)
    slice_cpp_str = lookup_cpp_type(slice_py_str, ret_imports)
    return v1 + slice_cpp_str + v2
