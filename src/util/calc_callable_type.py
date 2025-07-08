import ast

from src.d_types import AngInc
from src.util.handle_lists import handle_exprs
from src.util.ret_imports import RetImports, add_inc


def is_callable_type(node: ast.expr) -> bool:
    if (
        isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id == "Valu"
    ):
        return _is_callable_type(node.args[0])
    return _is_callable_type(node)


def _is_callable_type(node: ast.expr) -> bool:
    return (
        isinstance(node, ast.Subscript)
        and isinstance(node.value, ast.Name)
        and node.value.id == "Callable"
    )


def calc_callable_type(
    node: ast.Subscript | ast.Call,
    ret_imports: RetImports,
    handle_expr,
    in_header: bool = False,
) -> str:
    if isinstance(node, ast.Call):
        return (
            "Valu("
            + _calc_callable_type(node.args[0], ret_imports, handle_expr, in_header)
            + ")"
        )
    return _calc_callable_type(node, ret_imports, handle_expr, in_header)


def _calc_callable_type(
    node: ast.Subscript,
    ret_imports: RetImports,
    handle_expr,
    in_header: bool = False,
) -> str:
    add_inc(ret_imports, AngInc("functional"), in_header=in_header)
    assert isinstance(node.slice, ast.Tuple), "2 arguments required for Callable"
    assert len(node.slice.elts) == 2, "2 arguments required for Callable"
    arg_types = node.slice.elts[0]
    assert isinstance(arg_types, ast.List), "First argument for Callable must be a List"
    arg_types_cpp = handle_exprs(
        arg_types.elts, ret_imports, handle_expr, include_in_header=in_header
    )
    ret_type = node.slice.elts[1]
    ret_type_cpp = handle_expr(ret_type, ret_imports, in_header)
    if ret_type_cpp == "None":
        ret_type_cpp = "void"
    return f"std::function<{ret_type_cpp}({arg_types_cpp})> "
