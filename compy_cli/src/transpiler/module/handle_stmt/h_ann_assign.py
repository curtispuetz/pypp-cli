import ast

from compy_cli.src.transpiler.module.deps import Deps
from compy_cli.src.transpiler.module.handle_expr.h_comp import handle_comp
from compy_cli.src.transpiler.module.mapping.d_types import (
    CustomMappingEntry,
    CustomMappingFromLibEntry,
    CustomMappingStartsWithEntry,
    CustomMappingStartsWithFromLibEntry,
)
from compy_cli.src.transpiler.module.mapping.util import calc_string_fn, find_map_entry
from compy_cli.src.transpiler.module.util.calc_callable_type import calc_callable_type
from compy_cli.src.transpiler.module.util.inner_strings import calc_inside_ang, calc_inside_rd
from compy_cli.src.transpiler.module.util.calc_ref_string import calc_ref_str


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
    elif value_str == "PySet()":
        value_str = _empty_initialize("PySet", type_cpp)
    return _calc_final_str(d, value_str, const_str, type_cpp, target_str)


def _calc_final_str(
    d: Deps, value_str: str, const_str: str, type_cpp: str, target_str: str
):
    result_from_maps = _calc_result_from_maps_if_any(d, value_str, type_cpp, target_str)
    if result_from_maps is not None:
        return f"{const_str}{result_from_maps};"
    ref, type_cpp = calc_ref_str(type_cpp)
    return f"{const_str}{type_cpp}{ref} {target_str} = {value_str};"


def _calc_result_from_maps_if_any(
    d: Deps, value_str: str, type_cpp: str, target_str: str
) -> str | None:
    value_str_stripped: str = calc_inside_rd(value_str) if "(" in value_str else ""
    for k, v in d.maps.ann_assign.items():
        e = find_map_entry(v, d)
        if e is None:
            continue
        if isinstance(e, CustomMappingEntry):
            if type_cpp == k:
                d.add_incs(e.includes)
                return e.mapping_fn(type_cpp, target_str, value_str, value_str_stripped)
        elif isinstance(e, CustomMappingFromLibEntry):
            if type_cpp.startswith(k):
                d.add_incs(e.includes)
                return calc_string_fn(e)(
                    type_cpp, target_str, value_str, value_str_stripped
                )
        if isinstance(e, CustomMappingStartsWithEntry):
            if type_cpp.startswith(k):
                d.add_incs(e.includes)
                return e.mapping_fn(type_cpp, target_str, value_str, value_str_stripped)
        elif isinstance(e, CustomMappingStartsWithFromLibEntry):
            if type_cpp.startswith(k):
                d.add_incs(e.includes)
                return calc_string_fn(e)(
                    type_cpp, target_str, value_str, value_str_stripped
                )
    return None


def _empty_initialize(s: str, type_cpp: str):
    return f"{s}<{calc_inside_ang(type_cpp)}>" + "({})"
