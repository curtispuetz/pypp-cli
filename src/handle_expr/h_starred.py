import ast

from src.util.ret_imports import RetImports


def handle_starred(
    node: ast.Starred, ret_imports: RetImports, handle_expr, func_name: str
) -> str:
    value_str: str = handle_expr(node.value, ret_imports)
    return f"std::apply({func_name}, {value_str}.raw())"
