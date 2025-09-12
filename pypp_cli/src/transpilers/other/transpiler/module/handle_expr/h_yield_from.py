import ast

from pypp_cli.src.transpilers.other.transpiler.deps import Deps


def handle_yield_from(node: ast.YieldFrom, d: Deps) -> str:
    # Note: I don't need to add the dependency of "pypp_util/generator.h" because that
    #  is already done when the function with yield is defined.
    if node.value is None:
        d.value_err("'yield from' without value not supported", node)
    # Note: Imports will never be in header.
    value: str = d.handle_expr(node.value)
    return f"PYPP_CO_YIELD_FROM({value})"
