import ast

from src.d_types import CppInclude
from src.mapping.types import lookup_cpp_type


def handle_fn_def(
    node: ast.FunctionDef,
    ret_imports: set[CppInclude],
    ret_h_file: list[str],
    handle_stmt,
    handle_expr,
) -> str:
    # TODO: redo this using the current recursive approach
    # returns a list of strings that is the function lines of code, and
    # also returns a list of imports that should be appended
    fn_signature = _calc_fn_signature(node, ret_imports, handle_expr)
    ret_h_file.append(fn_signature + ";")
    body: list[str] = []
    for body_node in node.body:
        body.append(handle_stmt(body_node, ret_imports, ret_h_file))
    body_str = " ".join(body)
    return f"{fn_signature} {{{body_str}}}"


def _calc_fn_signature(
    node: ast.FunctionDef, ret_imports: set[CppInclude], handle_expr
) -> str:
    cpp_ret_type: str
    if node.returns is None:
        cpp_ret_type = "void"
    else:
        py_return_type = handle_expr(node.returns, ret_imports)
        cpp_ret_type = lookup_cpp_type(py_return_type, ret_imports)
    fn_name: str = node.name
    cpp_args: list[str] = []
    for py_arg in node.args.args:
        arg_name: str = py_arg.arg
        assert py_arg.annotation is not None, "function argument type must be specified"
        # TODO: extract this two function calls to a helper method
        py_arg_type = handle_expr(py_arg.annotation, ret_imports)
        cpp_arg_type = lookup_cpp_type(py_arg_type, ret_imports)
        cpp_args.append(f"{cpp_arg_type} {arg_name}")
    cpp_args_str = ", ".join(cpp_args)
    return f"{cpp_ret_type} {fn_name}({cpp_args_str})"
