import ast

from src.d_types import CppInclude
from src.mapping.fn_arg import lookup_cpp_fn_arg
from src.util.handle_lists import handle_stmts


def handle_fn_def(
    node: ast.FunctionDef,
    ret_imports: set[CppInclude],
    ret_h_file: list[str],
    handle_stmt,
    handle_expr,
) -> str:
    fn_signature = _calc_fn_signature(node, ret_imports, handle_expr)
    ret_h_file.append(fn_signature + ";")
    body_str: str = handle_stmts(node.body, ret_imports, ret_h_file, handle_stmt)
    return f"{fn_signature} {{{body_str}}}"


def _calc_fn_signature(
    node: ast.FunctionDef, ret_imports: set[CppInclude], handle_expr
) -> str:
    cpp_ret_type: str
    if node.returns is None:
        cpp_ret_type = "void"
    else:
        cpp_ret_type = handle_expr(node.returns, ret_imports)
    fn_name: str = node.name
    cpp_args: list[str] = []
    for py_arg in node.args.args:
        arg_name: str = py_arg.arg
        assert py_arg.annotation is not None, "function argument type must be specified"
        py_arg_type: str = handle_expr(py_arg.annotation, ret_imports)
        is_const: bool = True
        if py_arg_type.startswith("PyppMut(") and py_arg_type.endswith(")"):
            py_arg_type = _calc_inner_str(py_arg_type)
            is_const = False
        cpp_arg = lookup_cpp_fn_arg(py_arg_type, is_const)
        cpp_args.append(f"{cpp_arg} {arg_name}")
    cpp_args_str = ", ".join(cpp_args)
    return f"{cpp_ret_type} {fn_name}({cpp_args_str})"


def _calc_inner_str(s: str) -> str:
    return s.split("(", 1)[1][:-1]
