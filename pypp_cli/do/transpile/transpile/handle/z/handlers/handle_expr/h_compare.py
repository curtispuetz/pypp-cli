import ast
from dataclasses import dataclass

from pypp_cli.do.transpile.transpile.handle.node import Deps
from pypp_cli.do.transpile.transpile.handle.z.handlers.handle_other.cmpop import (
    handle_cmpop,
)


@dataclass(frozen=True, slots=True)
class CompareHandler:
    _d: Deps

    def handle(self, node: ast.Compare) -> str:
        left = node.left
        self._d.handle_expr(left)
        if len(node.comparators) != 1 or len(node.ops) != 1:
            self._d.value_err("Multiple comparators are not supported", node)
        right = node.comparators[0]
        left_str = self._d.handle_expr(left)
        right_str = self._d.handle_expr(right)
        op = node.ops[0]
        if isinstance(op, ast.In):
            return f"{right_str}.contains({left_str})"
        if isinstance(op, ast.NotIn):
            return f"!{right_str}.contains({left_str})"
        if isinstance(op, ast.Is):
            return f"&{left_str} == &{right_str}"
        if isinstance(op, ast.IsNot):
            return f"&{left_str} != &{right_str}"
        op_str = handle_cmpop(op)
        return f"{left_str} {op_str} {right_str}"
