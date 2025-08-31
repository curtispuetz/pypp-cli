import ast

from compy_cli.src.transpilers.other.module.deps import Deps
from compy_cli.src.transpilers.other.module.handle_other.operator import handle_operator


def handle_bin_op(node: ast.BinOp, d: Deps):
    left_op, middle_op, right_op = handle_operator(node.op, d)
    _left = d.handle_expr(node.left)
    left = f"({_left})" if isinstance(node.left, ast.BinOp) else _left
    _right = d.handle_expr(node.right)
    right = f"({_right})" if isinstance(node.right, ast.BinOp) else _right
    return f"{left_op}{left}{middle_op}{right}{right_op}"
