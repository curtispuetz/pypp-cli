import ast

from pypp_cli.do.transpile.transpile.handle.node import Deps
from pypp_cli.do.transpile.transpile.z_i.maps.d_types import (
    CustomMappingEntry,
    CustomMappingFromLibEntry,
    CustomMappingStartsWithEntry,
    CustomMappingStartsWithFromLibEntry,
)
from ...handle_expr.h_comp import CompHandler
from .direct_initializers import calc_value_str_for_direct_init
from .list_init_fns import calc_value_str_for_list_init_fns
from ...mapping.util import calc_string_fn, find_map_entry
from ...util.calc_callable_type import CallableTypeCalculator
from ...util.inner_strings import calc_inside_rd
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class GeneralAnnAssignHandler:
    _d: Deps
    _comp_handler: CompHandler
    _callable_type_calculator: CallableTypeCalculator

    def handle(self, node: ast.AnnAssign, target_str: str, prefix_str: str = "") -> str:
        type_cpp: str | None = self._callable_type_calculator.calc(node.annotation)
        if type_cpp is None:
            type_cpp = self._d.handle_expr(node.annotation)
        if node.value is None:
            return f"{type_cpp} {target_str};"
        if isinstance(node.value, (ast.ListComp, ast.SetComp, ast.DictComp)):
            return f"{type_cpp} {target_str}; " + self._comp_handler.handle(
                node.value, target_str
            )
        value_str, direct_initialize = self._calc_value_str(node, node.value)
        return self._calc_final_str(
            value_str, prefix_str, type_cpp, target_str, direct_initialize
        )

    def _calc_value_str(self, node: ast.AnnAssign, value: ast.expr) -> tuple[str, bool]:
        value_str: str | None = calc_value_str_for_list_init_fns(node, self._d)
        if value_str is None:
            value_str = self._d.handle_expr(value)
            direct_initialize = False
        else:
            direct_initialize = True

        new_value_str = calc_value_str_for_direct_init(node, value_str)
        if new_value_str is not None:
            direct_initialize = True
            value_str = new_value_str
        return value_str, direct_initialize

    def _calc_final_str(
        self,
        value_str: str,
        prefix_str: str,
        type_cpp: str,
        target_str: str,
        direct_initialize: bool,
    ):
        result_from_maps = self._calc_result_from_maps_if_any(
            value_str, type_cpp, target_str
        )
        if result_from_maps is not None:
            return f"{prefix_str}{result_from_maps};"
        if type_cpp.startswith("&"):
            type_cpp = type_cpp[1:] + "&"
        if direct_initialize:
            return f"{prefix_str}{type_cpp} {target_str}({value_str});"
        return f"{prefix_str}{type_cpp} {target_str} = {value_str};"

    def _calc_result_from_maps_if_any(
        self, value_str: str, type_cpp: str, target_str: str
    ) -> str | None:
        value_str_stripped: str = calc_inside_rd(value_str) if "(" in value_str else ""
        for k, v in self._d.maps.ann_assign.items():
            e = find_map_entry(v, self._d)
            if e is None:
                continue
            if isinstance(e, CustomMappingEntry):
                if type_cpp == k:
                    self._d.add_incs(e.includes)
                    return e.mapping_fn(
                        type_cpp, target_str, value_str, value_str_stripped
                    )
            elif isinstance(e, CustomMappingFromLibEntry):
                if type_cpp.startswith(k):
                    self._d.add_incs(e.includes)
                    return calc_string_fn(e)(
                        type_cpp, target_str, value_str, value_str_stripped
                    )
            if isinstance(e, CustomMappingStartsWithEntry):
                if type_cpp.startswith(k):
                    self._d.add_incs(e.includes)
                    return e.mapping_fn(
                        type_cpp, target_str, value_str, value_str_stripped
                    )
            elif isinstance(e, CustomMappingStartsWithFromLibEntry):
                if type_cpp.startswith(k):
                    self._d.add_incs(e.includes)
                    return calc_string_fn(e)(
                        type_cpp, target_str, value_str, value_str_stripped
                    )
        return None
