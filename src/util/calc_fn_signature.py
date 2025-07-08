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
    cpp_args_str = _calc_cpp_args_str(
        node, ret_imports, handle_expr, in_header, skip_first_arg
    )
    return f"{cpp_ret_type} {fn_name}({cpp_args_str})"


def _calc_cpp_args_str(
    node: ast.FunctionDef,
    ret_imports: RetImports,
    handle_expr,
    in_header: bool,
    skip_first_arg: bool = False,
) -> str:
    ret: list[str] = []
    cpp_arg_types = calc_fn_arg_types(
        node, ret_imports, handle_expr, in_header, skip_first_arg
    )
    for n, t in cpp_arg_types.items():
        ret.append(f"{t} {n}")
    return ", ".join(ret)


def calc_fn_arg_types(
    node: ast.FunctionDef,
    ret_imports: RetImports,
    handle_expr,
    in_header: bool,
    skip_first_arg: bool = False,
) -> dict[str, str]:
    ret = {}
    for i in range(skip_first_arg, len(node.args.args)):
        py_arg = node.args.args[i]
        arg_name: str = py_arg.arg
        assert py_arg.annotation is not None, (
            f"function argument {arg_name} must have type annotation"
        )
        cpp_arg_type: str = handle_expr(
            py_arg.annotation,
            ret_imports,
            include_in_header=in_header,
        )
        cpp_arg = lookup_cpp_fn_arg(cpp_arg_type)
        ret[arg_name] = cpp_arg
    return ret


def calc_fn_str_with_body(fn_signature: str, body_str: str) -> str:
    return f"{fn_signature} " + "{" + body_str + "}\n\n"
