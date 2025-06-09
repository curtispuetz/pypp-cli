import ast

from src.d_types import CppInclude


def handle_ann_assign(
    node: ast.AnnAssign, ret_imports: set[CppInclude], handle_expr
) -> str:
    type_cpp: str = handle_expr(node.annotation, ret_imports)
    target_str = handle_expr(node.target, ret_imports)
    if node.value is None:
        return f"{type_cpp} {target_str};"
    value_str = handle_expr(node.value, ret_imports)
    if type_cpp.startswith("PyDict<"):
        return f"{type_cpp} {target_str}({value_str});"
    return f"{type_cpp} {target_str} = {value_str};"
