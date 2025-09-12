import ast

from pypp_cli.src.transpilers.other.transpiler.deps import Deps


def handle_return(node: ast.Return, d: Deps) -> str:
    if node.value is None:
        return "return;"
    return_expr = d.handle_expr(node.value)
    return f"return {return_expr};"
