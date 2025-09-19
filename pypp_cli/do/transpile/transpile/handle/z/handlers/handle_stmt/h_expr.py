import ast
from dataclasses import dataclass

from pypp_cli.do.transpile.transpile.handle.node import Deps


@dataclass(frozen=True, slots=True)
class ExprStmtHandler:
    _d: Deps

    def handle(self, node: ast.Expr) -> str:
        return self._d.handle_expr(node.value) + ";"
