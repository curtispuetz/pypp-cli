import ast

from pypp_cli.src.transpilers.other.transpiler.deps import Deps

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class RaiseHandler:
    _d: Deps

    def handle(self, node: ast.Raise) -> str:
        if node.cause is not None:
            self._d.value_err(
                "exception cause (i.e. `raise ... from ...`) not supported", node
            )
        if node.exc is None:
            if self._d.inside_except_block:
                return "throw;"
            self._d.value_err(
                "a bare `raise` statement is only supported inside a except block", node
            )
        exc_str = self._d.handle_expr(node.exc)
        return f"throw {exc_str};"
