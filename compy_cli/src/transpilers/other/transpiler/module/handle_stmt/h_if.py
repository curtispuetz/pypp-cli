import ast

from compy_cli.src.transpilers.other.transpiler.deps import Deps


def handle_if(node: ast.If, d: Deps) -> str:
    test_str = d.handle_expr(node.test)
    body_str = d.handle_stmts(node.body)
    if len(node.orelse) == 0:
        return "if (" + test_str + ") {" + body_str + "}"
    if len(node.orelse) == 1:
        or_else = node.orelse[0]
        if isinstance(or_else, ast.If):
            return _if_else_body(test_str, body_str) + handle_if(or_else, d)
    or_else_str = d.handle_stmts(node.orelse)
    return _if_else_body(test_str, body_str) + "{" + or_else_str + "}"


def _if_else_body(test_str: str, body_str: str) -> str:
    return "if (" + test_str + ") {" + body_str + "} else "
