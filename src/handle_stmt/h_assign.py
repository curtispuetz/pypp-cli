import ast

from src.d_types import CppInclude


def handle_assign(node: ast.Assign, ret_imports: set[CppInclude], handle_expr):
    assert len(node.targets) == 1, "Not supported"
    target_str = handle_expr(node.targets[0], ret_imports)
    value_str = handle_expr(node.value, ret_imports)
    return f"{target_str} = {value_str};"
