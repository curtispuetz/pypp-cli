import ast

from src.deps import Deps


def handle_return(node: ast.Return, d: Deps) -> str:
    return_expr = d.handle_expr(node.value)
    return f"return {return_expr};"
