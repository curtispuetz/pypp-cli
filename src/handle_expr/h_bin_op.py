import ast

from src.deps import Deps
from src.handle_other.operator import handle_operator


def handle_bin_op(
    node: ast.BinOp,
    d: Deps,
    include_in_header: bool,
):
    left_op, middle_op, right_op = handle_operator(node.op, d)
    _left = d.handle_expr(node.left, include_in_header)
    left = f"({_left})" if isinstance(node.left, ast.BinOp) else _left
    _right = d.handle_expr(node.right, include_in_header)
    right = f"({_right})" if isinstance(node.right, ast.BinOp) else _right
    return f"{left_op}{left}{middle_op}{right}{right_op}"
