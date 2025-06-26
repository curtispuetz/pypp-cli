import ast

from src.util.ret_imports import RetImports


def handle_attribute(
    node: ast.Attribute,
    ret_imports: RetImports,
    handle_expr,
    include_in_header: bool,
):
    assert isinstance(node.attr, str), "Not supported"
    attr_str: str = node.attr
    if attr_str == "union":
        attr_str += "_"
    value_str = handle_expr(node.value, ret_imports, include_in_header)
    ret = f"{value_str}.{attr_str}"
    return ret
