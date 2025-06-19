import ast

from src.util.ret_imports import RetImports


def handle_stmt_expr(node: ast.Expr, ret_imports: RetImports, handle_expr) -> str:
    expr = handle_expr(node.value, ret_imports)
    return expr + ";"
