import ast

from src.handle_other.operator import handle_operator
from src.d_types import CppInclude


def handle_bin_op(node: ast.BinOp, ret_imports: set[CppInclude], handle_expr):
    left_op, middle_op, right_op = handle_operator(node.op, ret_imports)
    _left = handle_expr(node.left, ret_imports)
    left = f"({_left})" if isinstance(node.left, ast.BinOp) else _left
    _right = handle_expr(node.right, ret_imports)
    right = f"({_right})" if isinstance(node.right, ast.BinOp) else _right
    return f"{left_op}{left}{middle_op}{right}{right_op}"
