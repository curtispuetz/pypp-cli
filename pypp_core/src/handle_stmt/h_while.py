import ast

from pypp_core.src.deps import Deps
from pypp_core.src.util.handle_lists import handle_stmts


def handle_while(node: ast.While, d: Deps) -> str:
    assert len(node.orelse) == 0, "While loop else not supported"
    body_str = handle_stmts(node.body, d)
    test_str = d.handle_expr(node.test)
    return f"while ({test_str})" + "{" + body_str + "}"
