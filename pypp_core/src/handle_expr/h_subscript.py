import ast

from pypp_core.src.deps import Deps
from pypp_core.src.handle_expr.h_tuple import handle_tuple_inner_args
from pypp_core.src.mapping.subscript_value import lookup_cpp_subscript_value_type


def handle_subscript(
    node: ast.Subscript,
    d: Deps,
    include_in_header: bool,
) -> str:
    value_cpp_str = d.handle_expr(node.value, include_in_header)
    if value_cpp_str == "PyDefaultDict":
        assert isinstance(node.slice, ast.Tuple), (
            "defaultdict must be called as defaultdict[KeyType, ValueType]"
        )
        assert len(node.slice.elts) == 2, "2 types expected when calling defaultdict"
        default_dict_types = handle_tuple_inner_args(node.slice, d, include_in_header)
        return f"PyDefaultDict<{default_dict_types}>"
    if isinstance(node.slice, ast.Tuple):
        slice_cpp_str = handle_tuple_inner_args(node.slice, d, include_in_header)
    else:
        slice_cpp_str: str = d.handle_expr(node.slice, include_in_header)
    v1, v2 = lookup_cpp_subscript_value_type(value_cpp_str, d)
    return v1 + slice_cpp_str + v2
