import ast
from dataclasses import dataclass

from pypp_cli.src.transpilers.other.transpiler.deps import Deps
from pypp_cli.src.transpilers.other.transpiler.module.handle_other.operator import (
    OperatorHandler,
)


@dataclass(frozen=True, slots=True)
class AugAssignHandler:
    _d: Deps
    _operator_handler: OperatorHandler

    def handle(self, node: ast.AugAssign) -> str:
        op = self._operator_handler.handle_for_aug_assign(node.op)
        target = self._d.handle_expr(node.target)
        value = self._d.handle_expr(node.value)
        return f"{target} {op}= {value};"
