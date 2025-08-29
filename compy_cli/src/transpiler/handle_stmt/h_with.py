import ast

from compy_cli.src.transpiler.deps import Deps
from compy_cli.src.transpiler.handle_other.with_item import handle_with_item


def handle_with(node: ast.With, d: Deps):
    first_line = handle_with_item(node.items, d)
    body_str = d.handle_stmts(node.body)
    return "{" + f"{first_line} {body_str}" + "}"
