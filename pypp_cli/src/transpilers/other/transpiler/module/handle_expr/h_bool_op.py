import ast

from pypp_cli.src.transpilers.other.transpiler.deps import Deps
from pypp_cli.src.transpilers.other.transpiler.module.handle_other.bool_op import (
    handle_bool_op_type,
)

# ast docs: boolop = And | Or


def handle_bool_op(node: ast.BoolOp, d: Deps) -> str:
    op_str: str = handle_bool_op_type(node.op)
    return "(" + d.handle_exprs(node.values, f" {op_str} ") + ")"
