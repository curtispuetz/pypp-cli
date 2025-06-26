import ast

from src.d_types import QInc
from src.util.ret_imports import RetImports, add_inc


def handle_slice(
    node: ast.Slice,
    ret_imports: RetImports,
    handle_expr,
    include_in_header: bool,
):
    # NOTE: The C++ code handles Nones for start, but this code just wont use that.
    # Which is maybe fine
    add_inc(ret_imports, QInc("slice/creators.h"), include_in_header)
    lower: str = (
        "0"
        if node.lower is None
        else handle_expr(node.lower, ret_imports, include_in_header)
    )
    step: str = (
        "1"
        if node.step is None
        else handle_expr(node.step, ret_imports, include_in_header)
    )
    upper: str = (
        "std::nullopt"
        if node.upper is None
        else handle_expr(node.upper, ret_imports, include_in_header)
    )
    return f"py_slice({lower}, {upper}, {step})"
