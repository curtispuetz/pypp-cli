import ast
from dataclasses import dataclass

from pypp_cli.do.transpile.transpile.calc_code.z.deps import Deps


@dataclass(frozen=True, slots=True)
class YieldFromHandler:
    _d: Deps

    def handle(self, node: ast.YieldFrom) -> str:
        # Note: I don't need to add the dependency of "pypp_util/generator.h" because
        # that is already done when the function with yield is defined.
        if node.value is None:
            self._d.value_err("'yield from' without value not supported", node)
        # Note: Imports will never be in header.
        value: str = self._d.handle_expr(node.value)
        return f"PYPP_CO_YIELD_FROM({value})"
