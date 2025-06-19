import ast

from src.handle_other.operator import handle_operator
from src.util.ret_imports import RetImports


def handle_bin_op(
    node: ast.BinOp,
    ret_imports: RetImports,
    handle_expr,
    include_in_header: bool,
):
    left_op, middle_op, right_op = handle_operator(node.op, ret_imports)
    _left = handle_expr(node.left, ret_imports, include_in_header)
    left = f"({_left})" if isinstance(node.left, ast.BinOp) else _left
    _right = handle_expr(node.right, ret_imports, include_in_header)
    right = f"({_right})" if isinstance(node.right, ast.BinOp) else _right
    return f"{left_op}{left}{middle_op}{right}{right_op}"
