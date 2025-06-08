import ast

from src._types.operator import lookup_op
from src.d_types import CppInclude


def handle_bin_op(node: ast.BinOp, ret_imports: set[CppInclude], handle_expr):
    op = lookup_op(node.op)
    _left = handle_expr(node.left, ret_imports)
    left = f"({_left})" if isinstance(node.left, ast.BinOp) else _left
    _right = handle_expr(node.right, ret_imports)
    right = f"({_right})" if isinstance(node.right, ast.BinOp) else _right
    return f"{left} {op} {right}"
