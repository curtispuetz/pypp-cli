import ast

from src.d_types import AngInc
from src.deps import Deps
from src.util.ret_imports import add_inc


def handle_attribute(
    node: ast.Attribute,
    d: Deps,
    include_in_header: bool,
):
    assert isinstance(node.attr, str), "Not supported"
    attr_str: str = node.attr
    if attr_str == "union":
        attr_str += "_"
    value_str = d.handle_expr(node.value, include_in_header)
    if value_str == "self":
        return attr_str
    if value_str == "math":
        if attr_str == "pi":
            add_inc(d.ret_imports, AngInc("numbers"), include_in_header)
            return "std::numbers::pi"
        if attr_str == "radians":
            add_inc(d.ret_imports, AngInc("numbers"), include_in_header)
            return "(std::numbers::pi / 180.0) * "
        add_inc(d.ret_imports, AngInc("cmath"), include_in_header)
        return f"std::{attr_str}"
    return f"{value_str}.{attr_str}"
