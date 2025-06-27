import ast

from src.util.ret_imports import RetImports


def handle_yield_from(
    node: ast.YieldFrom,
    ret_imports: RetImports,
    handle_expr,
) -> str:
    assert node.value is not None, "Not supported"
    value: str = handle_expr(node.value, ret_imports)
    return f"CO_YIELD_FROM({value})"