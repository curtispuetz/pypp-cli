import ast
from dataclasses import dataclass

from pypp_cli.src.transpilers.other.transpiler.deps import Deps


def _if_else_body(test_str: str, body_str: str) -> str:
    return "if (" + test_str + ") {" + body_str + "} else "


@dataclass(frozen=True, slots=True)
class IfHandler:
    _d: Deps

    def handle(self, node: ast.If) -> str:
        test_str = self._d.handle_expr(node.test)
        body_str = self._d.handle_stmts(node.body)
        if len(node.orelse) == 0:
            return "if (" + test_str + ") {" + body_str + "}"
        if len(node.orelse) == 1:
            or_else = node.orelse[0]
            if isinstance(or_else, ast.If):
                return _if_else_body(test_str, body_str) + self.handle(or_else)
        or_else_str = self._d.handle_stmts(node.orelse)
        return _if_else_body(test_str, body_str) + "{" + or_else_str + "}"
