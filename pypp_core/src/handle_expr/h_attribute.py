import ast

from pypp_core.src.d_types import AngInc, PyImport
from pypp_core.src.deps import Deps
from pypp_core.src.mapping.attributes import lookup_cpp_attribute


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
    if d.is_imported(PyImport("math")) and value_str == "math":
        if attr_str == "pi":
            d.add_inc(AngInc("numbers"), include_in_header)
            return "std::numbers::pi"
        if attr_str == "radians":
            d.add_inc(AngInc("numbers"), include_in_header)
            return "(std::numbers::pi / 180.0) * "
        d.add_inc(AngInc("cmath"), include_in_header)
        return f"std::{attr_str}"
    ret = f"{value_str}.{attr_str}"
    return lookup_cpp_attribute(ret, d, include_in_header)
