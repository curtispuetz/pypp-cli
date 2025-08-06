import ast

from src.d_types import QInc
from src.deps import Deps
from src.util.ret_imports import add_inc


def handle_slice(
    node: ast.Slice,
    d: Deps,
    include_in_header: bool,
):
    # NOTE: The C++ code handles Nones for start, but this code just wont use that.
    # Which is maybe fine
    add_inc(d.ret_imports, QInc("slice/creators.h"), include_in_header)
    lower: str = (
        "0" if node.lower is None else d.handle_expr(node.lower, include_in_header)
    )
    step: str = (
        "1" if node.step is None else d.handle_expr(node.step, include_in_header)
    )
    upper: str = (
        "std::nullopt"
        if node.upper is None
        else d.handle_expr(node.upper, include_in_header)
    )
    return f"py_slice({lower}, {upper}, {step})"
