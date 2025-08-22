import ast

from pypp_core.src.deps import Deps
from pypp_core.src.handle_expr.h_starred import handle_call_with_starred_arg
from pypp_core.src.mapping.info_types import (
    CallMapInfoCppCall,
    CallMapInfoCustomMapping,
    CallMapInfoCustomMappingFromLibrary,
    CallMapInfoCustomMappingStartsWith,
    CallMapInfoCustomMappingStartsWithFromLibrary,
    CallMapInfoLeftAndRight,
    CallMapInfoReplaceDotWithDoubleColon,
)
from pypp_core.src.mapping.util import calc_string_fn, find_map_info


def handle_call(node: ast.Call, d: Deps) -> str:
    assert len(node.keywords) == 0, "keywords for a call are not supported."
    caller_str: str = d.handle_expr(node.func)
    # TODO: rename _type to something like caller
    for _type, r in d.maps.calls.items():
        info = find_map_info(r, d)
        if info is None:
            continue
        if isinstance(info, CallMapInfoCppCall):
            if caller_str == _type:
                d.add_incs(info.includes)
                return f"{info.cpp_call}({d.handle_exprs(node.args)})"
        elif isinstance(info, CallMapInfoLeftAndRight):
            if caller_str == _type:
                d.add_incs(info.includes)
                return info.left + d.handle_exprs(node.args) + info.right
        elif isinstance(info, CallMapInfoCustomMapping):
            if caller_str == _type:
                d.add_incs(info.includes)
                return info.mapping_fn(node, d)
        elif isinstance(info, CallMapInfoCustomMappingFromLibrary):
            if caller_str == _type:
                d.add_incs(info.includes)
                return calc_string_fn(info, "calls_map")(node, d)
        elif isinstance(info, CallMapInfoCustomMappingStartsWith):
            if caller_str.startswith(_type):
                d.add_incs(info.includes)
                return info.mapping_fn(node, d, caller_str)
        elif isinstance(info, CallMapInfoCustomMappingStartsWithFromLibrary):
            if caller_str.startswith(_type):
                d.add_incs(info.includes)
                return calc_string_fn(info, "calls_map")(node, d, caller_str)
        elif isinstance(info, CallMapInfoReplaceDotWithDoubleColon):
            if caller_str.startswith(_type):
                d.add_incs(info.includes)
                caller_str = caller_str.replace(".", "::")
                return f"{caller_str}({d.handle_exprs(node.args)})"
    return f"{caller_str}({d.handle_exprs(node.args)})"


# TODO later: support starred arguments
def _handle_call_with_starred_arg(
    node: ast.Call, d: Deps, caller_str: str
) -> str | None:
    if len(node.args) == 1:
        first_arg = node.args[0]
        if isinstance(first_arg, ast.Starred):
            assert len(node.args) == 1, (
                "Only one argument is allowed when using a starred argument."
            )
            return handle_call_with_starred_arg(first_arg, d, caller_str)
    return None
