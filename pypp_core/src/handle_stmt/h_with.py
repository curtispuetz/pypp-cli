import ast

from pypp_core.src.deps import Deps
from pypp_core.src.handle_other.with_item import handle_with_item
from pypp_core.src.util.handle_lists import handle_stmts


def handle_with(node: ast.With, d: Deps):
    first_line = handle_with_item(node.items, d)
    body_str = handle_stmts(node.body, d)
    return "{" + f"{first_line} {body_str}" + "}"
