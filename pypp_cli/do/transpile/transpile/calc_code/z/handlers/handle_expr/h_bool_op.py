import ast
from dataclasses import dataclass

from pypp_cli.do.transpile.transpile.calc_code.z.deps import Deps
from pypp_cli.do.transpile.transpile.calc_code.z.handlers.handle_other.bool_op import (
    handle_bool_op_type,
)

# ast docs: boolop = And | Or


@dataclass(frozen=True, slots=True)
class BoolOpHandler:
    _d: Deps

    def handle(self, node: ast.BoolOp) -> str:
        op_str: str = handle_bool_op_type(node.op)
        return "(" + self._d.handle_exprs(node.values, f" {op_str} ") + ")"
