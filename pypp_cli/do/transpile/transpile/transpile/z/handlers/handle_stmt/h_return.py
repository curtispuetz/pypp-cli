import ast

from pypp_cli.do.transpile.transpile.transpile.node import Deps


from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ReturnHandler:
    _d: Deps

    def handle(self, node: ast.Return) -> str:
        if node.value is None:
            return "return;"
        return_expr = self._d.handle_expr(node.value)
        return f"return {return_expr};"
