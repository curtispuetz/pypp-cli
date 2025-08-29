import ast

from compy_cli.src.transpiler.deps import Deps
from compy_cli.src.transpiler.handle_other.cmpop import handle_cmpop


def handle_compare(node: ast.Compare, d: Deps) -> str:
    left = node.left
    assert len(node.comparators) == 1, "Not supported"
    right = node.comparators[0]
    left_str = d.handle_expr(left)
    right_str = d.handle_expr(right)
    assert len(node.ops) == 1, "Not supported"
    op = node.ops[0]
    if isinstance(op, ast.In):
        return f"{right_str}.contains({left_str})"
    if isinstance(op, ast.NotIn):
        return f"!{right_str}.contains({left_str})"
    op_str = handle_cmpop(op)
    return f"{left_str} {op_str} {right_str}"
