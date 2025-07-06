import ast

from src.handle_expr.h_tuple import handle_tuple_inner_args
from src.util.ret_imports import RetImports


def handle_assign(node: ast.Assign, ret_imports: RetImports, handle_expr):
    assert len(node.targets) == 1, "Not supported"
    if isinstance(node.targets[0], ast.Tuple):
        ts = handle_tuple_inner_args(node.targets[0], ret_imports, handle_expr)
        target_str: str = f"const auto &[{ts}]"
    else:
        target_str: str = handle_expr(node.targets[0], ret_imports)
    value_str: str = handle_expr(node.value, ret_imports)
    return f"{target_str} = {value_str};"
