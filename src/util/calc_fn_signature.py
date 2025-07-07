import ast

from src.d_types import QInc
from src.mapping.fn_arg import lookup_cpp_fn_arg
from src.util.inner_strings import calc_inside_sq, calc_inside_rd
from src.util.ret_imports import RetImports, add_inc


def calc_fn_signature(
    node: ast.FunctionDef,
    ret_imports: RetImports,
    handle_expr,
    fn_name: str,
    in_header: bool,
    skip_first_arg: bool = False,
) -> str:
    cpp_ret_type: str
    if node.returns is None:
        cpp_ret_type = "void"
    else:
        cpp_ret_type = handle_expr(
            node.returns,
            ret_imports,
            include_in_header=in_header,
        )
        if cpp_ret_type.startswith("Iterator[") and cpp_ret_type.endswith("]"):
            add_inc(
                ret_imports,
                QInc("pypp_util/generator.h"),
                in_header=in_header,
            )
            cpp_ret_type = f"Generator<{calc_inside_sq(cpp_ret_type)}>"
        elif cpp_ret_type.startswith("Ref(") and cpp_ret_type.endswith(")"):
            cpp_ret_type = calc_inside_rd(cpp_ret_type) + "&"
    cpp_args: list[str] = []
    for i in range(skip_first_arg, len(node.args.args)):
        py_arg = node.args.args[i]
        arg_name: str = py_arg.arg
        assert py_arg.annotation is not None, "function argument type must be specified"
        py_arg_type: str = handle_expr(
            py_arg.annotation,
            ret_imports,
            include_in_header=in_header,
        )
        is_pass_by_value: bool = True
        if py_arg_type.startswith("Valu(") and py_arg_type.endswith(")"):
            py_arg_type = calc_inside_rd(py_arg_type)
            is_pass_by_value = False
        cpp_arg = lookup_cpp_fn_arg(py_arg_type, is_pass_by_value)
        cpp_args.append(f"{cpp_arg} {arg_name}")
    cpp_args_str = ", ".join(cpp_args)
    return f"{cpp_ret_type} {fn_name}({cpp_args_str})"


def calc_fn_str_with_body(fn_signature: str, body_str: str) -> str:
    return f"{fn_signature} " + "{" + body_str + "}"
