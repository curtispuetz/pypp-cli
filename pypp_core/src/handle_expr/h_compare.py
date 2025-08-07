import ast

from pypp_core.src.deps import Deps
from pypp_core.src.handle_other.cmpop import handle_cmpop


def handle_compare(
    node: ast.Compare,
    d: Deps,
    include_in_header: bool,
) -> str:
    left = node.left
    assert len(node.comparators) == 1, "Not supported"
    right = node.comparators[0]
    left_str = d.handle_expr(left, include_in_header)
    right_str = d.handle_expr(right, include_in_header)
    assert len(node.ops) == 1, "Not supported"
    op = node.ops[0]
    if isinstance(op, ast.In):
        return f"{right_str}.contains({left_str})"
    if isinstance(op, ast.NotIn):
        return f"!{right_str}.contains({left_str})"
    op_str = handle_cmpop(op)
    return f"{left_str} {op_str} {right_str}"
