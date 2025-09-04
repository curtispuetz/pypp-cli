import ast

from pypp_cli.src.transpilers.other.transpiler.deps import Deps


def handle_lambda(node: ast.Lambda, d: Deps) -> str:
    args: str = ", ".join("auto " + a.arg for a in node.args.args)
    body_str: str = d.handle_expr(node.body)
    return f"[]({args}) " + "{ return " + body_str + "; }"
