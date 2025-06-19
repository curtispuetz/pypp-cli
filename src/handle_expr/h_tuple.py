import ast

from src.util.handle_lists import handle_exprs
from src.util.ret_imports import RetImports


def handle_tuple(
    node: ast.Tuple,
    ret_imports: RetImports,
    handle_expr,
    include_in_header: bool,
) -> str:
    # Note for later: The node.ctx will tell you if you are loading values
    #  like a, b, c = my_fn(). So I can use it for that.
    return (
        "PyTup("
        + handle_exprs(node.elts, ret_imports, handle_expr, include_in_header)
        + ")"
    )
