import ast

from src.d_types import CppInclude
from src.mapping.calls import lookup_cpp_call


def handle_call(
    node: ast.Call, ret_imports: set[CppInclude], handle_expr, handle_exprs
):
    caller_str = handle_expr(node.func, ret_imports)
    cpp_call_start, cpp_call_end = lookup_cpp_call(caller_str, ret_imports)
    args_str = handle_exprs(node.args, ret_imports)
    return f"{cpp_call_start}{args_str}{cpp_call_end}"
