import ast

from pypp_cli.src.transpilers.other.transpiler.deps import Deps
from pypp_cli.src.transpilers.other.transpiler.module.handle_expr.h_tuple import (
    handle_tuple_inner_args,
)


def handle_assign(node: ast.Assign, d: Deps):
    assert len(node.targets) == 1, (
        "More than one target for an assignment is not supported"
    )
    target = node.targets[0]
    if isinstance(target, ast.Subscript) and isinstance(target.slice, ast.Slice):
        raise ValueError("Slice assignment is not supported")
    if isinstance(target, ast.Tuple):
        ts = handle_tuple_inner_args(target, d)
        target_str: str = f"auto [{ts}]"
    else:
        target_str: str = d.handle_expr(target)
    value_str: str = d.handle_expr(node.value)
    return f"{target_str} = {value_str};"
