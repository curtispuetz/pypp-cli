import ast

from pypp_core.src.deps import Deps
from pypp_core.src.handle_expr.h_call.transpile_list import CALLS_TRANSPILE
from pypp_core.src.handle_expr.h_starred import handle_call_with_starred_arg
from pypp_core.src.mapping.calls import lookup_cpp_call


def handle_call(node: ast.Call, d: Deps):
    assert len(node.keywords) == 0, "keywords for a call are not supported."
    caller_str: str = d.handle_expr(node.func, skip_cpp_lookup=True)
    # TODO: for bridge library creation, you let users define a function to run if a
    # condition is met.
    for t in CALLS_TRANSPILE:
        if d.is_imported(t.imp):
            if t.fn is not None:
                if caller_str == t.caller_str:
                    return t.fn(node, d)
            elif t.fn_starts_with is not None:
                if caller_str.startswith(t.caller_str):
                    return t.fn_starts_with(node, d, caller_str)
            else:
                assert t.replace_dot_with_double_colon_include is not None, (
                    "Shouldn't happen"
                )
                if caller_str.startswith(t.caller_str):
                    d.add_inc(t.replace_dot_with_double_colon_include)
                    caller_str = caller_str.replace(".", "::")
                    break

    r = _handle_call_with_starred_arg(node, d, caller_str)
    if r is not None:
        return r
    args_str = d.handle_exprs(node.args)
    cpp_call_start, cpp_call_end = lookup_cpp_call(caller_str, d)
    return f"{cpp_call_start}{args_str}{cpp_call_end}"


def _handle_call_with_starred_arg(
    node: ast.Call, d: Deps, caller_str: str
) -> str | None:
    if len(node.args) == 1:
        first_arg = node.args[0]
        if isinstance(first_arg, ast.Starred):
            return handle_call_with_starred_arg(first_arg, d, caller_str)
    return None
