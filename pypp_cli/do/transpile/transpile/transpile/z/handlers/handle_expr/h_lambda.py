import ast
from dataclasses import dataclass

from pypp_cli.do.transpile.transpile.transpile.node import Deps


@dataclass(frozen=True, slots=True)
class LambdaHandler:
    _d: Deps

    def handle(self, node: ast.Lambda) -> str:
        args: str = ", ".join("auto " + a.arg for a in node.args.args)
        body_str: str = self._d.handle_expr(node.body)
        return f"[]({args}) " + "{ return " + body_str + "; }"
