import ast

from compy_cli.src.d_types import AngInc, PyImport
from compy_cli.src.deps import Deps
from compy_cli.src.mapping.attributes import lookup_cpp_attribute


def handle_attribute(node: ast.Attribute, d: Deps):
    assert isinstance(node.attr, str), "Not supported"
    attr_str: str = node.attr
    if attr_str == "union":  # This is for the set.union method.
        attr_str += "_"
    value_str = d.handle_expr(node.value)
    if value_str == "self":
        return attr_str
    if d.is_imported(PyImport("math")) and value_str == "math":
        if attr_str == "pi":
            d.add_inc(AngInc("numbers"))
            return "std::numbers::pi"
        if attr_str == "radians":
            d.add_inc(AngInc("numbers"))
            return "(std::numbers::pi / 180.0) * "
        d.add_inc(AngInc("cmath"))
        return f"std::{attr_str}"
    ret = f"{value_str}.{attr_str}"
    return lookup_cpp_attribute(ret, d)
