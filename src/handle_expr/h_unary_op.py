import ast

from src.handle_other.unary_op import handle_unaryop
from src.util.ret_imports import RetImports


def handle_unary_op(
    node: ast.UnaryOp,
    ret_imports: RetImports,
    handle_expr,
    include_in_header: bool,
) -> str:
    op_str = handle_unaryop(node.op)
    value = handle_expr(node.operand, ret_imports, include_in_header)
    return op_str + value
