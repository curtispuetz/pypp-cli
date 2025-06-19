import ast

from src.handle_other.with_item import handle_with_item
from src.util.handle_lists import handle_stmts
from src.util.ret_imports import RetImports


def handle_with(
    node: ast.With,
    ret_imports: RetImports,
    ret_h_file: list[str],
    handle_stmt,
    handle_expr,
):
    first_line = handle_with_item(node.items, ret_imports, handle_expr)
    body_str = handle_stmts(node.body, ret_imports, ret_h_file, handle_stmt)
    return "{" + f"{first_line} {body_str}" + "}"
