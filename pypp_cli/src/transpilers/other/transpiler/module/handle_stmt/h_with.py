import ast

from pypp_cli.src.transpilers.other.transpiler.deps import Deps


from dataclasses import dataclass

from pypp_cli.src.transpilers.other.transpiler.module.handle_other.with_item import (
    WithItemHandler,
)


@dataclass(frozen=True, slots=True)
class WithHandler:
    _d: Deps
    _with_item_handler: WithItemHandler

    def handle(self, node: ast.With) -> str:
        first_line = self._with_item_handler.handle(node.items)
        body_str = self._d.handle_stmts(node.body)
        return "{" + f"{first_line} {body_str}" + "}"
