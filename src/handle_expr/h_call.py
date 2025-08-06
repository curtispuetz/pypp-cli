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
    # TODO: for library creation, you let users define a function to run if a condition
    #  is met.
    if caller_str == "tg":
        assert len(node.args) == 2, "tg should have 2 arguments"
        add_inc(ret_imports, AngInc("any"), include_in_header)
        tuple_arg = handle_expr(node.args[0], ret_imports)
        index_arg = handle_expr(node.args[1], ret_imports)
        return f"{tuple_arg}.get<{index_arg}>()"
    if caller_str == "dg":
        assert len(node.args) == 2, "dg should have 2 arguments"
        dict_arg = handle_expr(node.args[0], ret_imports)
        index_arg = handle_expr(node.args[1], ret_imports)
        return f"{dict_arg}.dg({index_arg})"
    if caller_str == "ug":
        assert len(node.args) == 2, "ug should have 2 arguments"
        union_arg = handle_expr(node.args[0], ret_imports)
        type_arg = handle_expr(node.args[1], ret_imports)
        return f"{union_arg}.ug<{type_arg}>()"
    if caller_str == "isinst":
        assert len(node.args) == 2, "isinst should have 2 arguments"
        obj_arg = handle_expr(node.args[0], ret_imports)
        type_arg = handle_expr(node.args[1], ret_imports)
        return f"{obj_arg}.isinst<{type_arg}>()"
    if caller_str == "is_none":
        assert len(node.args) == 1, "is_none should have 1 argument"
        obj_arg = handle_expr(node.args[0], ret_imports)
        return f"{obj_arg}.is_none()"
    if caller_str == "list_reserve":
        assert len(node.args) == 2, "list_reserve should have 2 arguments"
        list_arg = handle_expr(node.args[0], ret_imports)
        size_arg = handle_expr(node.args[1], ret_imports)
        return f"{list_arg}.reserve({size_arg})"
    if len(node.args) == 1 and isinstance(node.args[0], ast.Starred):
        return handle_starred(node.args[0], ret_imports, handle_expr, caller_str)
    if caller_str.startswith("os."):
        add_inc(ret_imports, QInc("pypp_os.h"), include_in_header)
        caller_str = caller_str.replace(".", "::")
    elif caller_str.startswith("shutil."):
        add_inc(ret_imports, QInc("pypp_shutil.h"), include_in_header)
        caller_str = caller_str.replace(".", "::")
    elif caller_str.startswith("pypp_time."):
        add_inc(ret_imports, QInc("pypp_time.h"), include_in_header)
        caller_str = caller_str.replace(".", "::")
    args_str = handle_exprs(node.args, ret_imports, handle_expr, include_in_header)
    cpp_call_start, cpp_call_end = lookup_cpp_call(
        caller_str, ret_imports, include_in_header
    )
    return f"{cpp_call_start}{args_str}{cpp_call_end}"
