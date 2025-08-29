import ast

from compy_cli.src.transpiler.module.deps import Deps
from compy_cli.src.transpiler.module.handle_other.unary_op import handle_unaryop


def handle_unary_op(node: ast.UnaryOp, d: Deps) -> str:
    op_str = handle_unaryop(node.op)
    value = d.handle_expr(node.operand)
    return op_str + value
