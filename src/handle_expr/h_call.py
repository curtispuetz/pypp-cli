import ast

from src.d_types import CppInclude
from src.mapping.calls import lookup_cpp_call
from src.util.handle_lists import handle_exprs


def handle_call(node: ast.Call, ret_imports: set[CppInclude], handle_expr):
    caller_str = handle_expr(node.func, ret_imports)
    cpp_call_start, cpp_call_end = lookup_cpp_call(caller_str, ret_imports)
    if caller_str == "print":
        assert len(node.args) == 1, "only one argument supported for print statements"
        if isinstance(node.args[0], ast.BinOp):
            cpp_call_start = "("
            cpp_call_end = ")" + cpp_call_end
    args_str = handle_exprs(node.args, ret_imports, handle_expr)
    return f"{cpp_call_start}{args_str}{cpp_call_end}"
