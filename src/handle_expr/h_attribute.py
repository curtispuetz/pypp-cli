import ast

from src.d_types import CppInclude
from src.mapping.attributes import lookup_cpp_attr


def handle_attribute(node: ast.Attribute, ret_imports: set[CppInclude], handle_expr):
    assert isinstance(node.attr, str), "Not supported"
    cpp_attr = lookup_cpp_attr(node.attr)
    value_str = handle_expr(node.value, ret_imports)
    return f"{value_str}.{cpp_attr}"
