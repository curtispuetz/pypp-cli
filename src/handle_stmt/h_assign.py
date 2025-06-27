import ast

from src.util.inner_strings import calc_inside_rd
from src.util.ret_imports import RetImports


def handle_assign(node: ast.Assign, ret_imports: RetImports, handle_expr):
    assert len(node.targets) == 1, "Not supported"
    target_str: str = handle_expr(node.targets[0], ret_imports)
    value_str: str = handle_expr(node.value, ret_imports)
    if target_str.startswith("PyTup(") and target_str.endswith(")"):
        target_str = f"const auto &[{calc_inside_rd(target_str)}]"
    return f"{target_str} = {value_str};"
