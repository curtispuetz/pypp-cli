import ast

from compy_cli.src.transpiler.deps import Deps


def handle_return(node: ast.Return, d: Deps) -> str:
    assert node.value is not None, "None return value is not supported"
    return_expr = d.handle_expr(node.value)
    return f"return {return_expr};"
