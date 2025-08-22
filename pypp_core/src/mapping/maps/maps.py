from dataclasses import dataclass

from pypp_core.src.mapping.maps.calc_ann_assigns_map import calc_ann_assigns_map
from pypp_core.src.pypp_dirs import PyppDirs
from pypp_core.src.mapping.maps.calc_attrs_map import calc_attrs_map
from pypp_core.src.mapping.maps.calc_calls_map import calc_calls_map
from pypp_core.src.mapping.maps.calc_fn_args_by_value import (
    calc_fn_args_passed_by_value,
)
from pypp_core.src.mapping.maps.calc_imports_map import (
    ImportsMap,
    calc_imports_map,
)
from pypp_core.src.mapping.maps.calc_names_map import calc_names_map
from pypp_core.src.mapping.info_types import (
    AnnAssignsMap,
    AttrsMap,
    CallsMap,
    FnArgsByValueMap,
    NamesMap,
    SubscriptableTypesMap,
)
from pypp_core.src.mapping.maps.calc_subscriptable_types import calc_subscriptable_types


@dataclass(frozen=True, slots=True)
class Maps:
    names: NamesMap
    calls: CallsMap
    attrs: AttrsMap
    fn_args_passed_by_value: FnArgsByValueMap
    subscriptable_types: SubscriptableTypesMap
    # TODO: rename to imports
    imports_map: ImportsMap
    ann_assigns: AnnAssignsMap


def calc_maps(proj_info: dict, dirs: PyppDirs) -> Maps:
    return Maps(
        calc_names_map(proj_info, dirs),
        calc_calls_map(proj_info, dirs),
        calc_attrs_map(proj_info, dirs),
        calc_fn_args_passed_by_value(proj_info, dirs),
        calc_subscriptable_types(proj_info, dirs),
        calc_imports_map(proj_info, dirs),
        calc_ann_assigns_map(proj_info, dirs),
    )
