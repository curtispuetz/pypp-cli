import ast

from src.d_types import AngInc
from src.deps import Deps
from src.util.handle_lists import handle_exprs


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
    d: Deps,
    in_header: bool = False,
) -> str:
    if isinstance(node, ast.Call):
        return "Valu(" + _calc_callable_type(node.args[0], d, in_header) + ")"
    return _calc_callable_type(node, d, in_header)


def _calc_callable_type(
    node: ast.Subscript,
    d: Deps,
    in_header: bool = False,
) -> str:
    d.add_inc(AngInc("functional"), in_header=in_header)
    assert isinstance(node.slice, ast.Tuple), "2 arguments required for Callable"
    assert len(node.slice.elts) == 2, "2 arguments required for Callable"
    arg_types = node.slice.elts[0]
    assert isinstance(arg_types, ast.List), "First argument for Callable must be a List"
    arg_types_cpp = handle_exprs(arg_types.elts, d, include_in_header=in_header)
    ret_type = node.slice.elts[1]
    ret_type_cpp = d.handle_expr(ret_type, in_header)
    if ret_type_cpp == "std::monostate":
        ret_type_cpp = "void"
    return f"std::function<{ret_type_cpp}({arg_types_cpp})> "
