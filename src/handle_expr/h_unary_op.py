import ast

from src.handle_other.unary_op import handle_unaryop
from src.d_types import CppInclude


def handle_unary_op(
    node: ast.UnaryOp, ret_imports: set[CppInclude], handle_expr
) -> str:
    op_str = handle_unaryop(node.op)
    value = handle_expr(node.operand, ret_imports)
    return op_str + value
