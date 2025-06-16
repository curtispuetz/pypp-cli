import ast

from src.handle_other.cmpop import handle_cmpop
from src.d_types import CppInclude


def handle_compare(node: ast.Compare, ret_imports: set[CppInclude], handle_expr) -> str:
    left = node.left
    assert len(node.comparators) == 1, "Not supported"
    right = node.comparators[0]
    left_str = handle_expr(left, ret_imports)
    right_str = handle_expr(right, ret_imports)
    assert len(node.ops) == 1, "Not supported"
    op = node.ops[0]
    if isinstance(op, ast.In):
        return f"{right_str}.contains({left_str})"
    op_str = handle_cmpop(op)
    return f"{left_str} {op_str} {right_str}"
