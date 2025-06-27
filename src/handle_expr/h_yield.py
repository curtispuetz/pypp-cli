import ast

from src.util.ret_imports import RetImports


def handle_yield(
    node: ast.Yield,
    ret_imports: RetImports,
    handle_expr,
) -> str:
    # Note: I don't need to add the dependency of "pypp_util/generator.h" because that
    #  is already done when the function with yield is defined.
    assert node.value is not None, "Not supported"
    value: str = handle_expr(node.value, ret_imports)
    return f"co_yield {value}"