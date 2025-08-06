import ast

from src.deps import Deps


def handle_lambda(
    node: ast.Lambda,
    d: Deps,
) -> str:
    args: str = ", ".join("auto " + a.arg for a in node.args.args)
    body_str: str = d.handle_expr(node.body, include_in_header=True)
    return f"[]({args}) " + "{ return " + body_str + "; }"
