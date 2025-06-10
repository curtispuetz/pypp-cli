import ast

from src.d_types import CppInclude


def handle_attribute(node: ast.Attribute, ret_imports: set[CppInclude], handle_expr):
    assert isinstance(node.attr, str), "Not supported"
    attr_str: str = node.attr
    if attr_str == "union":
        attr_str += "_"
    value_str = handle_expr(node.value, ret_imports)
    return f"{value_str}.{attr_str}"
