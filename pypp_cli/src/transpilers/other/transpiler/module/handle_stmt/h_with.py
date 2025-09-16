import ast

from pypp_cli.src.transpilers.other.transpiler.deps import Deps
from pypp_cli.src.transpilers.other.transpiler.module.handle_other.with_item import (
    handle_with_item,
)


from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class WithHandler:
    _d: Deps

    def handle(self, node: ast.With) -> str:
        first_line = handle_with_item(node.items, self._d)
        body_str = self._d.handle_stmts(node.body)
        return "{" + f"{first_line} {body_str}" + "}"
