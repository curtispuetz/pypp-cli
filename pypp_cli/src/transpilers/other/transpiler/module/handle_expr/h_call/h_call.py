import ast

from pypp_cli.src.transpilers.other.transpiler.d_types import PySpecificImpFrom
from pypp_cli.src.transpilers.other.transpiler.deps import Deps
from pypp_cli.src.transpilers.other.transpiler.module.handle_expr.h_starred import (
    handle_call_with_starred_arg,
)
from pypp_cli.src.transpilers.other.transpiler.maps.d_types import (
    ToStringEntry,
    CustomMappingEntry,
    CustomMappingFromLibEntry,
    CustomMappingStartsWithEntry,
    CustomMappingStartsWithFromLibEntry,
    LeftAndRightEntry,
    ReplaceDotWithDoubleColonEntry,
)
from pypp_cli.src.transpilers.other.transpiler.module.mapping.util import (
    calc_string_fn,
    find_map_entry,
)


def handle_call(node: ast.Call, d: Deps) -> str:
    assert len(node.keywords) == 0, "keywords for a call are not supported."
    caller_str: str = d.handle_expr(node.func)
    if caller_str == "Ref" and d.is_imported(PySpecificImpFrom("pypp_python", "Ref")):
        assert len(node.args) == 1, "Ref() must have exactly one argument."
        return f"&{d.handle_expr(node.args[0])}"
    for k, v in d.maps.call.items():
        e = find_map_entry(v, d)
        if e is None:
            continue
        if isinstance(e, ToStringEntry):
            if caller_str == k:
                d.add_incs(e.includes)
                return f"{e.to}({d.handle_exprs(node.args)})"
        elif isinstance(e, LeftAndRightEntry):
            if caller_str == k:
                d.add_incs(e.includes)
                return e.left + d.handle_exprs(node.args) + e.right
        elif isinstance(e, CustomMappingEntry):
            if caller_str == k:
                d.add_incs(e.includes)
                return e.mapping_fn(node, d)
        elif isinstance(e, CustomMappingFromLibEntry):
            if caller_str == k:
                d.add_incs(e.includes)
                return calc_string_fn(e)(node, d)
        elif isinstance(e, CustomMappingStartsWithEntry):
            if caller_str.startswith(k):
                d.add_incs(e.includes)
                return e.mapping_fn(node, d, caller_str)
        elif isinstance(e, CustomMappingStartsWithFromLibEntry):
            if caller_str.startswith(k):
                d.add_incs(e.includes)
                return calc_string_fn(e)(node, d, caller_str)
        elif isinstance(e, ReplaceDotWithDoubleColonEntry):
            if caller_str.startswith(k):
                d.add_incs(e.includes)
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
