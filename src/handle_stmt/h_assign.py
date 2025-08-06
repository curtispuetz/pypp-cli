import ast

from src.deps import Deps
from src.handle_expr.h_tuple import handle_tuple_inner_args


def handle_assign(
    node: ast.Assign,
    d: Deps,
    include_in_header: bool = False,
):
    assert len(node.targets) == 1, "Not supported"
    if isinstance(node.targets[0], ast.Tuple):
        ts = handle_tuple_inner_args(node.targets[0], d, include_in_header)
        target_str: str = f"auto [{ts}]"
    else:
        target_str: str = d.handle_expr(node.targets[0], include_in_header)
    value_str: str = d.handle_expr(node.value, include_in_header)
    return f"{target_str} = {value_str};"
