import ast

from pypp_core.src.deps import Deps
from pypp_core.src.handle_expr.h_comp import handle_comp
from pypp_core.src.util.calc_callable_type import calc_callable_type
from pypp_core.src.util.inner_strings import calc_inside_ang, calc_inside_rd
from pypp_core.src.util.util import calc_ref_str


def handle_ann_assign(node: ast.AnnAssign, d: Deps) -> str:
    target_str: str = d.handle_expr(node.target)
    is_const: bool = target_str.isupper()
    const_str: str = "const " if is_const else ""
    is_private: bool = target_str.startswith("_")
    is_header_only: bool = is_const and not is_private
    d.set_inc_in_h(is_header_only)
    if is_header_only and is_const:
        const_str = "inline const "
    result: str = handle_general_ann_assign(
        node,
        d,
        target_str,
        const_str,
    )
    d.set_inc_in_h(False)
    if is_header_only:
        d.ret_h_file.append(result)
        return ""
    return result


def handle_general_ann_assign(
    node: ast.AnnAssign,
    d: Deps,
    target_str: str,
    const_str: str = "",
) -> str:
    type_cpp: str | None = calc_callable_type(node.annotation, d)
    if type_cpp is None:
        type_cpp = d.handle_expr(node.annotation)
    if node.value is None:
        return f"{type_cpp} {target_str};"
    if isinstance(node.value, (ast.ListComp, ast.SetComp, ast.DictComp)):
        return f"{type_cpp} {target_str}; " + handle_comp(node.value, d, target_str)
    value_str = d.handle_expr(node.value)
    if value_str == "PyList({})":
        value_str = _empty_initialize("PyList", type_cpp)
    elif value_str == "set()":
        value_str = _empty_initialize("PySet", type_cpp)
    return _calc_final_str(value_str, const_str, type_cpp, target_str)


def _calc_final_str(value_str: str, const_str: str, type_cpp: str, target_str: str):
    # TODO: for bridge library creation, you let users define a function if a condition
    if type_cpp.startswith("PyDict<"):
        # TODO later: consider that dicts are handled differently here than lists
        #  and sets. It might be nice if they are handled the same, but it seems hard
        #  to make it so.
        return f"{const_str}{type_cpp} {target_str}({value_str});"
    if type_cpp.startswith("Uni<"):
        v: str = calc_inside_rd(value_str)
        if v == "std::monostate":
            v += "{}"
        return f"{const_str}{type_cpp} {target_str}({v});"
    ref, type_cpp = calc_ref_str(type_cpp)
    return f"{const_str}{type_cpp}{ref} {target_str} = {value_str};"


def _empty_initialize(s: str, type_cpp: str):
    return f"{s}<{calc_inside_ang(type_cpp)}>" + "({})"
