import ast

from src.d_types import AngInc
from src.handle_expr.h_comp import handle_comp
from src.util.handle_lists import handle_exprs
from src.util.inner_strings import calc_inside_ang
from src.util.ret_imports import RetImports, add_inc
from src.util.util import calc_ref_str


def handle_ann_assign(
    node: ast.AnnAssign,
    ret_imports: RetImports,
    ret_h_file: list[str],
    handle_expr,
    handle_stmt,
) -> str:
    if _is_callable_type(node.annotation):
        type_cpp: str = _calc_callable_type(node.annotation, ret_imports, handle_expr)
    else:
        type_cpp: str = handle_expr(node.annotation, ret_imports)
    target_str = handle_expr(node.target, ret_imports)
    if node.value is None:
        return f"{type_cpp} {target_str};"
    if isinstance(node.value, (ast.ListComp, ast.SetComp, ast.DictComp)):
        return f"{type_cpp} {target_str}; " + handle_comp(
            node.value, ret_imports, ret_h_file, handle_expr, handle_stmt, target_str
        )
    value_str = handle_expr(node.value, ret_imports)
    if value_str == "PyList({})":
        value_str = _empty_initialize("PyList", type_cpp)
    elif value_str == "set()":
        value_str = _empty_initialize("PySet", type_cpp)
    if type_cpp.startswith("PyDict<"):
        # TODO later: consider that dicts are handled differently here than lists
        #  and sets. It might be nice if they are handled the same, but it seems hard
        #  to make it so.
        return f"{type_cpp} {target_str}({value_str});"
    ref, type_cpp = calc_ref_str(type_cpp)
    return f"{type_cpp}{ref} {target_str} = {value_str};"


def _is_callable_type(node: ast.expr) -> bool:
    return (
        isinstance(node, ast.Subscript)
        and isinstance(node.value, ast.Name)
        and node.value.id == "Callable"
    )


def _calc_callable_type(
    node: ast.Subscript,
    ret_imports: RetImports,
    handle_expr,
) -> str:
    add_inc(ret_imports, AngInc("functional"))
    assert isinstance(node.slice, ast.Tuple), "2 arguments required for Callable"
    assert len(node.slice.elts) == 2, "2 arguments required for Callable"
    arg_types = node.slice.elts[0]
    assert isinstance(arg_types, ast.List), "First argument for Callable must be a List"
    arg_types_cpp = handle_exprs(arg_types.elts, ret_imports, handle_expr)
    ret_type = node.slice.elts[1]
    ret_type_cpp = handle_expr(ret_type, ret_imports)
    return f"std::function<{ret_type_cpp}({arg_types_cpp})> "


def _empty_initialize(s: str, type_cpp: str):
    return f"{s}<{calc_inside_ang(type_cpp)}>" + "({})"
