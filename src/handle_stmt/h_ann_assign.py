import ast

from src.d_types import CppInclude


def handle_ann_assign(
    node: ast.AnnAssign, ret_imports: set[CppInclude], handle_expr
) -> str:
    type_cpp: str = handle_expr(node.annotation, ret_imports)
    if type_cpp.startswith("PyppOpt[") and type_cpp.endswith("]"):
        type_cpp = "std::optional<" + _calc_inner_str(type_cpp) + ">"
    target_str = handle_expr(node.target, ret_imports)
    if node.value is None:
        return f"{type_cpp} {target_str};"
    value_str = handle_expr(node.value, ret_imports)
    if value_str == "PyList({})":
        value_str = _empty_initialize("PyList", type_cpp)
    elif value_str == "set()":
        value_str = _empty_initialize("PySet", type_cpp)
    if type_cpp.startswith("PyDict<"):
        # TODO later: consider that dicts are handle differently here than lists
        #  and sets. It might be nice if they are handled the same, but it seems hard.
        #  to make it so.
        return f"{type_cpp} {target_str}({value_str});"
    return f"{type_cpp} {target_str} = {value_str};"


def _empty_initialize(s: str, type_cpp: str):
    return f"{s}<{_calc_inner_str_sq(type_cpp)}>" + "({})"


# TODO: dry these repeated methods (not just in this file)
def _calc_inner_str_sq(s: str) -> str:
    return s.split("<", 1)[1][:-1]


def _calc_inner_str(s: str) -> str:
    return s.split("[", 1)[1][:-1]
