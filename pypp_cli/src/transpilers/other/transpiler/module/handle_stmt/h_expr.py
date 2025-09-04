import ast

from pypp_cli.src.transpilers.other.transpiler.deps import Deps


def handle_stmt_expr(node: ast.Expr, d: Deps) -> str:
    expr = d.handle_expr(node.value)
    return expr + ";"
