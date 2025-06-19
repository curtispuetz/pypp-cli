import ast

from src.d_types import QInc
from src.util.handle_lists import handle_exprs
from src.util.ret_imports import RetImports, add_inc


def handle_list(
    node: ast.List,
    ret_imports: RetImports,
    handle_expr,
    include_in_header: bool,
) -> str:
    add_inc(ret_imports, QInc("py_list.h"), include_in_header)
    return (
        "PyList({"
        + handle_exprs(node.elts, ret_imports, handle_expr, include_in_header)
        + "})"
    )
