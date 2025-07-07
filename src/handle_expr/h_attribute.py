import ast

from src.d_types import AngInc
from src.util.ret_imports import RetImports, add_inc


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
    if value_str == "self":
        return attr_str
    if value_str == "math":
        if attr_str == "pi":
            add_inc(ret_imports, AngInc("numbers"), include_in_header)
            return "std::numbers::pi"
        if attr_str == "radians":
            add_inc(ret_imports, AngInc("numbers"), include_in_header)
            return "(std::numbers::pi / 180.0) * "
        add_inc(ret_imports, AngInc("cmath"), include_in_header)
        return f"std::{attr_str}"
    return f"{value_str}.{attr_str}"
