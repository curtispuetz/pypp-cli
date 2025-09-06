import ast

from pypp_cli.src.transpilers.other.transpiler.deps import Deps


def handle_call_with_starred_arg(node: ast.Starred, d: Deps, func_name: str) -> str:
    value_str: str = d.handle_expr(node.value)
    # TODO: make a not about way the .raw() is.
    return f"std::apply({func_name}, {value_str}.raw())"
