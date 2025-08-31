import ast

from compy_cli.src.transpilers.other.module.deps import Deps


def handle_yield_from(node: ast.YieldFrom, d: Deps) -> str:
    # Note: I don't need to add the dependency of "compy_util/generator.h" because that
    #  is already done when the function with yield is defined.
    assert node.value is not None, "Not supported"
    # Note: Imports will never be in header.
    value: str = d.handle_expr(node.value)
    return f"CO_YIELD_FROM({value})"
