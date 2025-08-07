import ast

from pypp_core.src.deps import Deps
from pypp_core.src.handle_other.unary_op import handle_unaryop


def handle_unary_op(
    node: ast.UnaryOp,
    d: Deps,
    include_in_header: bool,
) -> str:
    op_str = handle_unaryop(node.op)
    value = d.handle_expr(node.operand, include_in_header)
    return op_str + value
