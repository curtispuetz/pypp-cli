import ast

from compy_cli.src.transpiler.module.deps import Deps


def handle_stmt_expr(node: ast.Expr, d: Deps) -> str:
    expr = d.handle_expr(node.value)
    return expr + ";"
