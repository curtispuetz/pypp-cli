import ast

from src.util.ret_imports import RetImports


def handle_return(node: ast.Return, ret_imports: RetImports, handle_expr) -> str:
    return_expr = handle_expr(node.value, ret_imports)
    return f"return {return_expr};"
