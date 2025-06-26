import ast

from src.d_types import AngInc, QInc
from src.mapping.calls import lookup_cpp_call
from src.util.handle_lists import handle_exprs
from src.util.ret_imports import RetImports, add_inc


def handle_call(
    node: ast.Call,
    ret_imports: RetImports,
    handle_expr,
    include_in_header: bool,
):
    caller_str: str = handle_expr(
        node.func,
        ret_imports,
        skip_cpp_lookup=True,
        include_in_header=include_in_header,
    )
    cpp_call_start, cpp_call_end = lookup_cpp_call(
        caller_str, ret_imports, include_in_header
    )
    if caller_str == "pypp_tg":
        assert len(node.args) == 2, "incorrect number of args when calling pypp_tg"
        add_inc(ret_imports, AngInc("any"), include_in_header)
        tuple_arg = handle_expr(node.args[0], ret_imports)
        index_arg = handle_expr(node.args[1], ret_imports)
        return f"{tuple_arg}.get<{index_arg}>()"
    elif caller_str == "pypp_dg":
        assert len(node.args) == 2, "incorrect number of args when calling pypp_dg"
        dict_arg = handle_expr(node.args[0], ret_imports)
        index_arg = handle_expr(node.args[1], ret_imports)
        return f"{dict_arg}.dg({index_arg})"
    elif caller_str == "pypp_get_resources":
        add_inc(ret_imports, QInc("pypp_resources.h"), include_in_header)
    args_str = handle_exprs(node.args, ret_imports, handle_expr, include_in_header)
    return f"{cpp_call_start}{args_str}{cpp_call_end}"
