import ast
from dataclasses import dataclass

from pypp_cli.src.transpilers.library.transpiler.deps import Deps
from pypp_cli.src.transpilers.library.transpiler.module.handle_other.unary_op import (
    handle_unaryop,
)


@dataclass(frozen=True, slots=True)
class UnaryOpHandler:
    _d: Deps

    def handle(self, node: ast.UnaryOp) -> str:
        op_str = handle_unaryop(node.op)
        value = self._d.handle_expr(node.operand)
        return op_str + value
