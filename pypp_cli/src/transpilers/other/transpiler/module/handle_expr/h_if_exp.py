import ast

from pypp_cli.src.transpilers.other.transpiler.deps import Deps


def handle_if_exp(node: ast.IfExp, d: Deps) -> str:
    test = d.handle_expr(node.test)
    body = d.handle_expr(node.body)
    orelse = d.handle_expr(node.orelse)
    return f"({test}) ? {body} : {orelse}"
