import ast

from src.d_types import AngInc
from src.deps import Deps
from src.util.handle_lists import handle_exprs


def _is_callable_type(node: ast.Subscript) -> bool:
    return isinstance(node.value, ast.Name) and node.value.id == "Callable"


def calc_callable_type(node: ast.expr, d: Deps, in_header: bool = False) -> str | None:
    if (
        isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id == "Valu"
    ):
        arg1 = node.args[0]
        if isinstance(arg1, ast.Subscript):
            if _is_callable_type(arg1):
                return "Valu(" + _calc_callable_type(arg1, d, in_header) + ")"
    if isinstance(node, ast.Subscript):
        if _is_callable_type(node):
            return _calc_callable_type(node, d, in_header)
    return None


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
