import ast

from pypp_cli.src.transpilers.other.transpiler.deps import Deps
from pypp_cli.src.transpilers.other.transpiler.module.handle_expr.h_tuple import (
    handle_tuple_inner_args,
)


def handle_assign(node: ast.Assign, d: Deps):
    if len(node.targets) != 1:
        d.value_err("Multiple assignment targets are not supported", node)
    target = node.targets[0]
    if isinstance(target, ast.Subscript) and isinstance(target.slice, ast.Slice):
        d.value_err("Slice assignment is not supported", node)
    if isinstance(target, ast.Tuple):
        ts = handle_tuple_inner_args(target, d)
        target_str: str = f"auto [{ts}]"
    else:
        target_str: str = d.handle_expr(target)
    value_str: str = d.handle_expr(node.value)
    return f"{target_str} = {value_str};"
