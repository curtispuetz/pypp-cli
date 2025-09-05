import ast

from pypp_cli.src.transpilers.other.transpiler.deps import Deps
from pypp_cli.src.transpilers.other.transpiler.module.handle_expr.h_comp import (
    handle_comp,
)
from pypp_cli.src.transpilers.other.transpiler.maps.d_types import (
    CustomMappingEntry,
    CustomMappingFromLibEntry,
    CustomMappingStartsWithEntry,
    CustomMappingStartsWithFromLibEntry,
)
from pypp_cli.src.transpilers.other.transpiler.module.mapping.util import (
    calc_string_fn,
    find_map_entry,
)
from pypp_cli.src.transpilers.other.transpiler.module.util.calc_callable_type import (
    calc_callable_type,
)
from pypp_cli.src.transpilers.other.transpiler.module.util.inner_strings import (
    calc_inside_rd,
)


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


# TODO: refactor
DIRECT_INITIALIZERS: dict[str, type] = {
    "PyList": ast.List,
    "PySet": ast.Set,
}


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
    direct_initialize: bool = False
    if (
        isinstance(node.value, ast.Call)
        and isinstance(node.value.func, ast.Name)
        and node.value.func.id == "set"
    ):
        direct_initialize = True
        value_str = "{}"
    else:
        value_str = d.handle_expr(node.value)

    i: int = value_str.find("(")
    if i != -1:
        func_name = value_str[:i]
        if func_name in DIRECT_INITIALIZERS and isinstance(
            node.value, DIRECT_INITIALIZERS[func_name]
        ):
            direct_initialize = True
            value_str = calc_inside_rd(value_str)
    return _calc_final_str(
        d, value_str, const_str, type_cpp, target_str, direct_initialize
    )


def _calc_final_str(
    d: Deps,
    value_str: str,
    const_str: str,
    type_cpp: str,
    target_str: str,
    direct_initialize: bool,
):
    result_from_maps = _calc_result_from_maps_if_any(d, value_str, type_cpp, target_str)
    if result_from_maps is not None:
        return f"{const_str}{result_from_maps};"
    if type_cpp.startswith("&"):
        type_cpp = type_cpp[1:] + "&"
    if direct_initialize:
        return f"{const_str}{type_cpp} {target_str}({value_str});"
    return f"{const_str}{type_cpp} {target_str} = {value_str};"


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
