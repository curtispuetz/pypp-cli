import ast
from dataclasses import dataclass

from pypp_cli.do.transpile.transpile.handle.node import Deps
from pypp_cli.do.transpile.transpile.handle.z.handlers.handle_other.operator import (
    OperatorHandler,
)


@dataclass(frozen=True, slots=True)
class BinOpHandler:
    _d: Deps
    _operator_handler: OperatorHandler

    def handle(self, node: ast.BinOp) -> str:
        left_op, middle_op, right_op = self._operator_handler.handle(node.op)
        _left = self._d.handle_expr(node.left)
        left = f"({_left})" if isinstance(node.left, ast.BinOp) else _left
        _right = self._d.handle_expr(node.right)
        right = f"({_right})" if isinstance(node.right, ast.BinOp) else _right
        return f"{left_op}{left}{middle_op}{right}{right_op}"
