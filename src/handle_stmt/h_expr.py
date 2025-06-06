import ast

from src.d_types import CppInclude


def handle_stmt_expr(node: ast.Expr, ret_imports: set[CppInclude], handle_expr) -> str:
    expr = handle_expr(node.value, ret_imports)
    return expr + ";"
