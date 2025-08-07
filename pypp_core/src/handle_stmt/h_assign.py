import ast

from pypp_core.src.deps import Deps
from pypp_core.src.handle_expr.h_tuple import handle_tuple_inner_args


def handle_assign(
    node: ast.Assign,
    d: Deps,
    include_in_header: bool = False,
):
    assert len(node.targets) == 1, "Not supported"
    target = node.targets[0]
    if isinstance(target, ast.Tuple):
        ts = handle_tuple_inner_args(target, d, include_in_header)
        target_str: str = f"auto [{ts}]"
    else:
        target_str: str = d.handle_expr(target, include_in_header)
    value_str: str = d.handle_expr(node.value, include_in_header)
    return f"{target_str} = {value_str};"
