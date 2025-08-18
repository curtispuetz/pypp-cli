import ast

from pypp_core.src.deps import Deps


def handle_yield(node: ast.Yield, d: Deps) -> str:
    # Note: I don't need to add the dependency of "pypp_util/generator.h" because that
    #  is already done when the function with yield is defined.
    assert node.value is not None, "Not supported"
    # TODO: should I not have the include in header option here?
    value: str = d.handle_expr(node.value)
    return f"co_yield {value}"
