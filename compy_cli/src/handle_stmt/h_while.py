import ast

from compy_cli.src.deps import Deps


def handle_while(node: ast.While, d: Deps) -> str:
    assert len(node.orelse) == 0, "While loop else not supported"
    body_str = d.handle_stmts(node.body)
    test_str = d.handle_expr(node.test)
    return f"while ({test_str})" + "{" + body_str + "}"
