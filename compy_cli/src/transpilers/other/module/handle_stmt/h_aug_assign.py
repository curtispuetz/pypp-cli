import ast

from compy_cli.src.transpilers.other.transpiler.deps import Deps
from compy_cli.src.transpilers.other.module.handle_other.operator import (
    handle_operator_for_aug_assign,
)


def handle_aug_assign(node: ast.AugAssign, d: Deps) -> str:
    op = handle_operator_for_aug_assign(node.op)
    target = d.handle_expr(node.target)
    value = d.handle_expr(node.value)
    return f"{target} {op}= {value};"
