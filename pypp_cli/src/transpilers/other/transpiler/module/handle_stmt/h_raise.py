import ast

from pypp_cli.src.transpilers.other.transpiler.deps import Deps


def handle_raise(node: ast.Raise, d: Deps) -> str:
    if node.cause is not None:
        d.value_err("exception cause (i.e. `raise ... from ...`) not supported", node)
    if node.exc is None:
        if d.inside_except_block:
            return "throw;"
        d.value_err(
            "a bare `raise` statement is only supported inside a except block", node
        )
    exc_str = d.handle_expr(node.exc)
    return f"throw {exc_str};"
