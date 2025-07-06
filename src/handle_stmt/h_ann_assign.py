import ast

from src.handle_expr.h_comp import handle_comp
from src.util.inner_strings import calc_inside_ang, calc_inside_rd
from src.util.ret_imports import RetImports


def handle_ann_assign(
    node: ast.AnnAssign,
    ret_imports: RetImports,
    ret_h_file: list[str],
    handle_expr,
    handle_stmt,
) -> str:
    type_cpp: str = handle_expr(node.annotation, ret_imports)
    target_str = handle_expr(node.target, ret_imports)
    if node.value is None:
        return f"{type_cpp} {target_str};"
    if isinstance(node.value, (ast.ListComp, ast.SetComp, ast.DictComp)):
        return f"{type_cpp} {target_str}; " + handle_comp(
            node.value, ret_imports, ret_h_file, handle_expr, handle_stmt, target_str
        )
    value_str = handle_expr(node.value, ret_imports)
    if value_str == "PyList({})":
        value_str = _empty_initialize("PyList", type_cpp)
    elif value_str == "set()":
        value_str = _empty_initialize("PySet", type_cpp)
    if type_cpp.startswith("PyDict<"):
        # TODO later: consider that dicts are handled differently here than lists
        #  and sets. It might be nice if they are handled the same, but it seems hard
        #  to make it so.
        return f"{type_cpp} {target_str}({value_str});"
    ref, type_cpp = _calc_ref_str(type_cpp)
    return f"{type_cpp}{ref} {target_str} = {value_str};"

def _calc_ref_str(type_cpp: str) -> tuple[str, str]:
    if type_cpp.startswith("Ref(") and type_cpp.endswith(")"):
        return "&", calc_inside_rd(type_cpp)
    return "", type_cpp

def _empty_initialize(s: str, type_cpp: str):
    return f"{s}<{calc_inside_ang(type_cpp)}>" + "({})"
