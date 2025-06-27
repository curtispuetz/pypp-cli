import ast

from src.util.handle_lists import handle_exprs
from src.util.ret_imports import RetImports


def handle_tuple_inner_args(
    node: ast.Tuple,
    ret_imports: RetImports,
    handle_expr,
    include_in_header: bool = False,
):
    return handle_exprs(node.elts, ret_imports, handle_expr, include_in_header)


def handle_tuple(
    node: ast.Tuple,
    ret_imports: RetImports,
    handle_expr,
    include_in_header: bool,
) -> str:
    # Note for later: The node.ctx will tell you if you are loading values
    #  like a, b, c = my_fn(). So I can use it for that.
    return f"PyTup({handle_tuple_inner_args(node, ret_imports, handle_expr, include_in_header)})"


# TODO: use implementation below
# args: list[str] = []
# for arg in node.elts:
#     x = handle_expr(arg, ret_imports, include_in_header)
#     if isinstance(arg, ast.Name):
#         x = "std::move(" + x + ")"
#     args.append(x)
# args_str: str = ", ".join(args)
# return f"PyTup({args_str})"
