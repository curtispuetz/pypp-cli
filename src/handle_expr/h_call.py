import ast

from src.d_types import CppInclude, AngInc, QInc
from src.mapping.calls import lookup_cpp_call
from src.util.handle_lists import handle_exprs


def handle_call(node: ast.Call, ret_imports: set[CppInclude], handle_expr):
    caller_str: str = handle_expr(node.func, ret_imports, skip_cpp_lookup=True)
    cpp_call_start, cpp_call_end = lookup_cpp_call(caller_str, ret_imports)
    if caller_str == "print":
        assert len(node.args) == 1, "only one argument supported for print statements"
        if isinstance(node.args[0], ast.BinOp):
            cpp_call_start = "("
            cpp_call_end = ")" + cpp_call_end
    elif caller_str == "pypp_print":
        # TODO later: I need to decide what to do with printing and how that should work
        assert len(node.args) == 1
        ret_imports.add(AngInc("iostream"))
        cpp_call_start = "std::cout << "
        cpp_call_end = " << std::endl"
    elif caller_str == "PyppOpt":
        if len(node.args) == 0:
            ret_imports.add(AngInc("optional"))
            return "std::nullopt"
        cpp_call_start = ""
        cpp_call_end = ""
    elif caller_str == "pypp_tg":
        assert len(node.args) == 2, "incorrect number of args when calling pypp_tg"
        ret_imports.add(AngInc("any"))
        tuple_arg = handle_expr(node.args[0], ret_imports)
        index_arg = handle_expr(node.args[1], ret_imports)
        return f"{tuple_arg}.get<{index_arg}>()"
    elif caller_str in {"pypp_dg_opt", "pypp_dg"}:
        assert len(node.args) == 2, "incorrect number of args when calling pypp_dg_opt"
        dict_arg = handle_expr(node.args[0], ret_imports)
        index_arg = handle_expr(node.args[1], ret_imports)
        return f"{dict_arg}.dg{'_opt' if caller_str.endswith('t') else ''}({index_arg})"
    elif caller_str.startswith("pypp_np") and caller_str.endswith(
        ("zeros", "ones", "full", "array")
    ):
        fn_name = caller_str[8:]
        ret_imports.add(QInc("np_arr.h"))
        cpp_dtype = handle_expr(node.args[-1], ret_imports)
        first_arg_str = handle_expr(node.args[0], ret_imports)
        if fn_name != "array":
            # in this case the first arg is a 'shape'
            first_arg_str = _add_size_t_to_shape_string(first_arg_str)
        args_str: list[str] = [first_arg_str]
        if fn_name == "full":
            fill_value = handle_expr(node.args[1], ret_imports)
            args_str.append(fill_value)
        return f"pypp_np::{fn_name}<{cpp_dtype}>({', '.join(args_str)})"
    args_str = handle_exprs(node.args, ret_imports, handle_expr)
    return f"{cpp_call_start}{args_str}{cpp_call_end}"


def _add_size_t_to_shape_string(shape_str: str):
    assert shape_str.startswith("PyList"), (
        "list should be used as the first parameter for pypp_np_* methods"
    )
    return shape_str[0:6] + "<size_t>" + shape_str[6:]
