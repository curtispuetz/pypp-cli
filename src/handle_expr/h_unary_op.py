import ast

from src._types.unary_op import lookup_unary_op
from src.d_types import CppInclude


def handle_unary_op(node: ast.UnaryOp, ret_imports: set[CppInclude], handle_expr) -> str:
    op_str = lookup_unary_op(node.op)
    value = handle_expr(node.operand, ret_imports)
    return op_str + value
