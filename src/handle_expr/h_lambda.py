import ast

from src.util.ret_imports import RetImports


def handle_lambda(
    node: ast.Lambda,
    ret_imports: RetImports,
    handle_expr,
) -> str:
    args: str = ", ".join("auto " + a.arg for a in node.args.args)
    body_str: str = handle_expr(node.body, ret_imports, include_in_header=True)
    return f"[]({args}) " + "{ return " + body_str + "; }"
