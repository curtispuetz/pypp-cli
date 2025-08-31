import ast

from compy_cli.src.transpilers.other.transpiler.deps import Deps
from compy_cli.src.transpilers.other.module.handle_expr.h_tuple import (
    handle_tuple_inner_args,
)


def handle_assign(node: ast.Assign, d: Deps):
    assert len(node.targets) == 1, "Not supported"
    target = node.targets[0]
    if isinstance(target, ast.Tuple):
        ts = handle_tuple_inner_args(target, d)
        target_str: str = f"auto [{ts}]"
    else:
        target_str: str = d.handle_expr(target)
    value_str: str = d.handle_expr(node.value)
    return f"{target_str} = {value_str};"
