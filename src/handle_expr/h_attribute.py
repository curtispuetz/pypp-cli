import ast

from src.d_types import CppInclude
from src.mapping.np_types import NP_TYPE_TO_CPP_TYPE


def handle_attribute(node: ast.Attribute, ret_imports: set[CppInclude], handle_expr):
    assert isinstance(node.attr, str), "Not supported"
    attr_str: str = node.attr
    if attr_str == "union":
        attr_str += "_"
    value_str = handle_expr(node.value, ret_imports)
    ret = f"{value_str}.{attr_str}"
    if ret in NP_TYPE_TO_CPP_TYPE:
        return NP_TYPE_TO_CPP_TYPE[ret]
    return ret
