import ast

from src.handle_other.operator import handle_operator_for_aug_assign
from src.d_types import CppInclude


def handle_aug_assign(
    node: ast.AugAssign, ret_imports: set[CppInclude], handle_expr
) -> str:
    op = handle_operator_for_aug_assign(node.op)
    target = handle_expr(node.target, ret_imports)
    value = handle_expr(node.value, ret_imports)
    return f"{target} {op}= {value};"
