import ast

from src.deps import Deps
from src.util.handle_lists import handle_stmts


def handle_if(node: ast.If, d: Deps) -> str:
    test_str = d.handle_expr(node.test)
    body_str = handle_stmts(node.body, d)
    if len(node.orelse) == 0:
        return "if (" + test_str + ") {" + body_str + "}"
    if len(node.orelse) == 1:
        or_else = node.orelse[0]
        if isinstance(or_else, ast.If):
            return _if_else_body(test_str, body_str) + handle_if(or_else, d)
    or_else_str = handle_stmts(node.orelse, d)
    return _if_else_body(test_str, body_str) + "{" + or_else_str + "}"


def _if_else_body(test_str: str, body_str: str) -> str:
    return "if (" + test_str + ") {" + body_str + "} else "
