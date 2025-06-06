import ast

from src.d_types import CppInclude


def handle_return(node: ast.Return, ret_imports: set[CppInclude], handle_expr) -> str:
    return_expr = handle_expr(node.value, ret_imports)
    return f"return {return_expr};"
