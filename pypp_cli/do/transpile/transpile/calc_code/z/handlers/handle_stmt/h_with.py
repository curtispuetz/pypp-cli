import ast
from dataclasses import dataclass

from ...deps import Deps
from ..handle_other.with_item import WithItemHandler


@dataclass(frozen=True, slots=True)
class WithHandler:
    _d: Deps
    _with_item_handler: WithItemHandler

    def handle(self, node: ast.With) -> str:
        first_line = self._with_item_handler.handle(node.items)
        body_str = self._d.handle_stmts(node.body)
        return "{" + f"{first_line} {body_str}" + "}"
