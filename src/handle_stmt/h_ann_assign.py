import ast

from src.d_types import CppInclude
from src.mapping.types import lookup_cpp_type


def handle_ann_assign(
    node: ast.AnnAssign, ret_imports: set[CppInclude], handle_expr
) -> str:
    type_py = handle_expr(node.annotation, ret_imports)
    type_cpp = lookup_cpp_type(type_py, ret_imports)
    target_str = handle_expr(node.target, ret_imports)
    if node.value is None:
        return f"{type_cpp} {target_str};"
    value_str = handle_expr(node.value, ret_imports)
    return f"{type_cpp} {target_str} = {value_str};"
