import ast

from src._types.operator import lookup_simple_op
from src.d_types import CppInclude


def handle_aug_assign(
    node: ast.AugAssign, ret_imports: set[CppInclude], handle_expr
) -> str:
    op = lookup_simple_op(node.op)
    target = handle_expr(node.target, ret_imports)
    value = handle_expr(node.value, ret_imports)
    return f"{target} {op}= {value};"
