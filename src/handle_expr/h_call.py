import ast

from src.d_types import CppInclude, QInc
from src.mapping.calls import lookup_cpp_call
from src.util.handle_lists import handle_exprs


def handle_call(node: ast.Call, ret_imports: set[CppInclude], handle_expr):
    caller_str = handle_expr(node.func, ret_imports, skip_cpp_lookup=True)
    cpp_call_start, cpp_call_end = lookup_cpp_call(caller_str, ret_imports)
    if caller_str == "print":
        assert len(node.args) == 1, "only one argument supported for print statements"
        if isinstance(node.args[0], ast.BinOp):
            cpp_call_start = "("
            cpp_call_end = ")" + cpp_call_end
    elif caller_str == "pypp_print":
        # TODO later: I need to decide what to do with printing and how that should work
        assert len(node.args) == 1
        ret_imports.add(QInc("iostream"))
        cpp_call_start = "std::cout << "
        cpp_call_end = " << std::endl"
    elif caller_str == "PyppOpt":
        if len(node.args) == 0:
            return "std::nullopt"
        cpp_call_start = ""
        cpp_call_end = ""
    args_str = handle_exprs(node.args, ret_imports, handle_expr)
    return f"{cpp_call_start}{args_str}{cpp_call_end}"
