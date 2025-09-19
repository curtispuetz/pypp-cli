import ast

from pypp_cli.do.transpile.transpile.transpile.node import Deps


from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class WhileHandler:
    _d: Deps

    def handle(self, node: ast.While) -> str:
        if len(node.orelse) != 0:
            self._d.value_err_no_ast("While loop else not supported")
        body_str = self._d.handle_stmts(node.body)
        test_str = self._d.handle_expr(node.test)
        return f"while ({test_str})" + "{" + body_str + "}"
