import ast

from compy_cli.src.deps import Deps
from compy_cli.src.handle_expr.h_starred import handle_call_with_starred_arg
from compy_cli.src.mapping.info_types import (
    ToStringEntry,
    CustomMappingEntry,
    CustomMappingFromLibEntry,
    CustomMappingStartsWithEntry,
    CustomMappingStartsWithFromLibEntry,
    LeftAndRightEntry,
    ReplaceDotWithDoubleColonEntry,
)
from compy_cli.src.mapping.util import calc_string_fn, find_map_info


def handle_call(node: ast.Call, d: Deps) -> str:
    assert len(node.keywords) == 0, "keywords for a call are not supported."
    caller_str: str = d.handle_expr(node.func)
    for caller, r in d.maps.call.items():
        info = find_map_info(r, d)
        if info is None:
            continue
        if isinstance(info, ToStringEntry):
            if caller_str == caller:
                d.add_incs(info.includes)
                return f"{info.to}({d.handle_exprs(node.args)})"
        elif isinstance(info, LeftAndRightEntry):
            if caller_str == caller:
                d.add_incs(info.includes)
                return info.left + d.handle_exprs(node.args) + info.right
        elif isinstance(info, CustomMappingEntry):
            if caller_str == caller:
                d.add_incs(info.includes)
                return info.mapping_fn(node, d)
        elif isinstance(info, CustomMappingFromLibEntry):
            if caller_str == caller:
                d.add_incs(info.includes)
                return calc_string_fn(info, "call_map")(node, d)
        elif isinstance(info, CustomMappingStartsWithEntry):
            if caller_str.startswith(caller):
                d.add_incs(info.includes)
                return info.mapping_fn(node, d, caller_str)
        elif isinstance(info, CustomMappingStartsWithFromLibEntry):
            if caller_str.startswith(caller):
                d.add_incs(info.includes)
                return calc_string_fn(info, "call_map")(node, d, caller_str)
        elif isinstance(info, ReplaceDotWithDoubleColonEntry):
            if caller_str.startswith(caller):
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
