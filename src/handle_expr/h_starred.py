import ast

from src.deps import Deps


def handle_starred(node: ast.Starred, d: Deps, func_name: str) -> str:
    value_str: str = d.handle_expr(node.value)
    return f"std::apply({func_name}, {value_str}.raw())"
