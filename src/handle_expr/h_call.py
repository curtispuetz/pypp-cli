import ast

from src.d_types import AngInc, QInc
from src.handle_expr.h_starred import handle_starred
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
    if caller_str == "pypp_tg":
        assert len(node.args) == 2, "incorrect number of args when calling pypp_tg"
        add_inc(ret_imports, AngInc("any"), include_in_header)
        tuple_arg = handle_expr(node.args[0], ret_imports)
        index_arg = handle_expr(node.args[1], ret_imports)
        return f"{tuple_arg}.get<{index_arg}>()"
    if caller_str == "pypp_dg":
        assert len(node.args) == 2, "incorrect number of args when calling pypp_dg"
        dict_arg = handle_expr(node.args[0], ret_imports)
        index_arg = handle_expr(node.args[1], ret_imports)
        return f"{dict_arg}.dg({index_arg})"
    if len(node.args) == 1 and isinstance(node.args[0], ast.Starred):
        return handle_starred(node.args[0], ret_imports, handle_expr, caller_str)
    args_str = handle_exprs(node.args, ret_imports, handle_expr, include_in_header)
    if caller_str.startswith("os."):
        add_inc(ret_imports, QInc("pypp_os.h"), include_in_header)
        caller_str = caller_str.replace(".", "::")
    elif caller_str.startswith("shutil."):
        add_inc(ret_imports, QInc("pypp_shutil.h"), include_in_header)
        caller_str = caller_str.replace(".", "::")
    elif caller_str.startswith("pypp_time"):
        add_inc(ret_imports, QInc("pypp_time.h"), include_in_header)
        caller_str = replace_second_underscore(caller_str)
    cpp_call_start, cpp_call_end = lookup_cpp_call(
        caller_str, ret_imports, include_in_header
    )
    # TODO: make this part of the previous if-elif block.
    if caller_str == "pypp_get_resources":
        add_inc(ret_imports, QInc("pypp_resources.h"), include_in_header)
    return f"{cpp_call_start}{args_str}{cpp_call_end}"


def replace_second_underscore(s):
    parts = s.split("_", 2)  # Split into at most 3 parts
    assert len(parts) >= 2, "Name cannot start with pypp_time"
    return parts[0] + "_" + parts[1] + "::" + parts[2]
