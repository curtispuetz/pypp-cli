import ast

from pypp_cli.do.transpile.transpile.handle.node import Deps


def handle_call_with_starred_arg(node: ast.Starred, d: Deps, func_name: str) -> str:
    # NOTE: This function is not used right now. Don't both with it again until it is
    # used. What is the .raw()?
    value_str: str = d.handle_expr(node.value)
    return f"std::apply({func_name}, {value_str}.raw())"
