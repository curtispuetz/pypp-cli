import ast
from dataclasses import dataclass

from pypp_cli.src.transpilers.other.transpiler.deps import Deps
from pypp_cli.src.transpilers.other.transpiler.module.handle_other.operator import (
    handle_operator,
)


@dataclass(frozen=True, slots=True)
class BinOpHandler:
    _d: Deps

    def handle(self, node: ast.BinOp) -> str:
        left_op, middle_op, right_op = handle_operator(node.op, self._d)
        _left = self._d.handle_expr(node.left)
        left = f"({_left})" if isinstance(node.left, ast.BinOp) else _left
        _right = self._d.handle_expr(node.right)
        right = f"({_right})" if isinstance(node.right, ast.BinOp) else _right
        return f"{left_op}{left}{middle_op}{right}{right_op}"
