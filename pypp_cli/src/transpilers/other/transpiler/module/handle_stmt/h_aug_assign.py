import ast
from dataclasses import dataclass

from pypp_cli.src.transpilers.other.transpiler.deps import Deps
from pypp_cli.src.transpilers.other.transpiler.module.handle_other.operator import (
    handle_operator_for_aug_assign,
)


@dataclass(frozen=True, slots=True)
class AugAssignHandler:
    _d: Deps

    def handle(self, node: ast.AugAssign) -> str:
        op = handle_operator_for_aug_assign(node.op, self._d)
        target = self._d.handle_expr(node.target)
        value = self._d.handle_expr(node.value)
        return f"{target} {op}= {value};"
