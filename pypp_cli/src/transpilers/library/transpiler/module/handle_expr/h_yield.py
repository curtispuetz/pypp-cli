import ast
from dataclasses import dataclass

from pypp_cli.src.transpilers.library.transpiler.deps import Deps


@dataclass(frozen=True, slots=True)
class YieldHandler:
    _d: Deps

    def handle(self, node: ast.Yield) -> str:
        # Note: I don't need to add the dependency of "pypp_util/generator.h" because
        # that is already done when the function with yield is defined.
        if node.value is None:
            return self._d.value_err("'yield' without value not supported", node)
        # Note: Imports will never be in header.
        value: str = self._d.handle_expr(node.value)
        return f"co_yield {value}"
