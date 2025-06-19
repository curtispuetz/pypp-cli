import ast

from src.d_types import QInc
from src.util.handle_lists import handle_exprs
from src.util.ret_imports import RetImports, add_inc


def handle_with_item(
    nodes: list[ast.withitem],
    ret_imports: RetImports,
    handle_expr,
) -> str:
    error_str: str = (
        "With statement can only be used as 'with open(arg1, ?optional_arg2) as name1'"
    )
    node, args = _assert_with_item_is_open(nodes, error_str)
    args_str = handle_exprs(args, ret_imports, handle_expr)
    variable_name = _assert_variable_name(node, error_str)
    add_inc(ret_imports, QInc("pypp_text_io.h"))
    return f"PyTextIO {variable_name}({args_str});"


def _assert_with_item_is_open(
    nodes: list[ast.withitem], error_str: str
) -> tuple[ast.withitem, list[ast.expr]]:
    assert len(nodes) == 1, error_str
    node = nodes[0]
    assert isinstance(node.context_expr, ast.Call), error_str
    assert isinstance(node.context_expr.func, ast.Name), error_str
    assert node.context_expr.func.id == "open", error_str
    assert len(node.context_expr.args) in {1, 2}, "open() expected 1 or 2 arguments"
    return node, node.context_expr.args


def _assert_variable_name(node: ast.withitem, error_str: str) -> str:
    assert node.optional_vars is not None, error_str
    assert isinstance(node.optional_vars, ast.Name), error_str
    assert isinstance(node.optional_vars.id, str), error_str
    return node.optional_vars.id
