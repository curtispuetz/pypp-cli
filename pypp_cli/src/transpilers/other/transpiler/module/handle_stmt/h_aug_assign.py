import ast

from pypp_cli.src.transpilers.other.transpiler.deps import Deps
from pypp_cli.src.transpilers.other.transpiler.module.handle_other.operator import (
    handle_operator_for_aug_assign,
)


def handle_aug_assign(node: ast.AugAssign, d: Deps) -> str:
    op = handle_operator_for_aug_assign(node.op)
    target = d.handle_expr(node.target)
    value = d.handle_expr(node.value)
    return f"{target} {op}= {value};"
