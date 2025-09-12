import ast

from pypp_cli.src.transpilers.other.transpiler.d_types import QInc
from pypp_cli.src.transpilers.other.transpiler.deps import Deps


_ERR_STR: str = (
    "With statement can only be used as 'with open(arg1, optional_arg2) as name1'"
)


def handle_with_item(nodes: list[ast.withitem], d: Deps) -> str:
    node, args = _assert_with_item_is_open(nodes, d)
    args_str = d.handle_exprs(args)
    variable_name = _get_var_name(node, d)
    d.add_inc(QInc("pypp_text_io.h"))
    return f"pypp::PyTextIO {variable_name}({args_str});"


def _assert_with_item_is_open(
    nodes: list[ast.withitem], d: Deps
) -> tuple[ast.withitem, list[ast.expr]]:
    if len(nodes) != 1:
        d.value_err_no_ast(_ERR_STR)
    node = nodes[0]
    if not isinstance(node.context_expr, ast.Call):
        d.value_err(_ERR_STR, node)
    elif not isinstance(node.context_expr.func, ast.Name):
        d.value_err(_ERR_STR, node)
    elif not node.context_expr.func.id == "open":
        d.value_err(_ERR_STR, node)
    elif len(node.context_expr.args) not in {1, 2}:
        d.value_err("open() expected 1 or 2 arguments", node)
    return node, node.context_expr.args


def _get_var_name(node: ast.withitem, d: Deps) -> str:
    if node.optional_vars is None:
        d.value_err(_ERR_STR, node)
    elif not isinstance(node.optional_vars, ast.Name):
        d.value_err(_ERR_STR, node)
    elif not isinstance(node.optional_vars.id, str):
        d.value_err(_ERR_STR, node)
    return node.optional_vars.id
