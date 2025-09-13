import ast

from pypp_cli.src.transpilers.other.transpiler.deps import Deps
from pypp_cli.src.transpilers.other.transpiler.maps.d_types import (
    CustomMappingEntry,
    CustomMappingFromLibEntry,
    CustomMappingStartsWithEntry,
    CustomMappingStartsWithFromLibEntry,
)
from pypp_cli.src.transpilers.other.transpiler.module.handle_expr.h_comp import (
    handle_comp,
)
from pypp_cli.src.transpilers.other.transpiler.module.handle_stmt.h_ann_assign.direct_initializers import (  # noqa: E501
    calc_value_str_for_direct_init,
)
from pypp_cli.src.transpilers.other.transpiler.module.handle_stmt.h_ann_assign.list_init_fns import (  # noqa: E501
    calc_value_str_for_list_init_fns,
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


def handle_general_ann_assign(
    node: ast.AnnAssign,
    d: Deps,
    target_str: str,
    prefix_str: str = "",
) -> str:
    type_cpp: str | None = calc_callable_type(node.annotation, d)
    if type_cpp is None:
        type_cpp = d.handle_expr(node.annotation)
    if node.value is None:
        return f"{type_cpp} {target_str};"
    if isinstance(node.value, (ast.ListComp, ast.SetComp, ast.DictComp)):
        return f"{type_cpp} {target_str}; " + handle_comp(node.value, d, target_str)
    value_str, direct_initialize = _calc_value_str(node, node.value, d)
    return _calc_final_str(
        d, value_str, prefix_str, type_cpp, target_str, direct_initialize
    )


def _calc_value_str(node: ast.AnnAssign, value: ast.expr, d: Deps) -> tuple[str, bool]:
    value_str: str | None = calc_value_str_for_list_init_fns(node, d)
    if value_str is None:
        value_str = d.handle_expr(value)
        direct_initialize = False
    else:
        direct_initialize = True

    new_value_str = calc_value_str_for_direct_init(node, value_str)
    if new_value_str is not None:
        direct_initialize = True
        value_str = new_value_str
    return value_str, direct_initialize


def _calc_final_str(
    d: Deps,
    value_str: str,
    prefix_str: str,
    type_cpp: str,
    target_str: str,
    direct_initialize: bool,
):
    result_from_maps = _calc_result_from_maps_if_any(d, value_str, type_cpp, target_str)
    if result_from_maps is not None:
        return f"{prefix_str}{result_from_maps};"
    if type_cpp.startswith("&"):
        type_cpp = type_cpp[1:] + "&"
    if direct_initialize:
        return f"{prefix_str}{type_cpp} {target_str}({value_str});"
    return f"{prefix_str}{type_cpp} {target_str} = {value_str};"


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
