import ast
from dataclasses import dataclass

from pypp_cli.do.transpile.transpile.handle.node import Deps


@dataclass(frozen=True, slots=True)
class IfExpHandler:
    _d: Deps

    def handle(self, node: ast.IfExp) -> str:
        test = self._d.handle_expr(node.test)
        body = self._d.handle_expr(node.body)
        orelse = self._d.handle_expr(node.orelse)
        return f"({test}) ? {body} : {orelse}"
