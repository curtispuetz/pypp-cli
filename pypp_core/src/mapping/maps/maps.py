from dataclasses import dataclass

from pypp_core.src.mapping.maps.calc_ann_assign_map import calc_ann_assign_map
from pypp_core.src.pypp_dirs import PyppDirs
from pypp_core.src.mapping.maps.calc_attr_map import calc_attr_map
from pypp_core.src.mapping.maps.calc_call_map import calc_call_map
from pypp_core.src.mapping.maps.calc_fn_arg_by_value_map import (
    calc_fn_arg_passed_by_value_map,
)
from pypp_core.src.mapping.maps.calc_import_map import (
    ImportMap,
    calc_import_map,
)
from pypp_core.src.mapping.maps.calc_name_map import calc_name_map
from pypp_core.src.mapping.info_types import (
    AnnAssignsMap,
    AttrMap,
    CallMap,
    FnArgByValueMap,
    NameMap,
    SubscriptableTypeMap,
)
from pypp_core.src.mapping.maps.calc_subscriptable_type_map import (
    calc_subscriptable_type_map,
)


@dataclass(frozen=True, slots=True)
class Maps:
    name: NameMap
    call: CallMap
    attr: AttrMap
    fn_arg_passed_by_value: FnArgByValueMap
    subscriptable_type: SubscriptableTypeMap
    import_: ImportMap
    ann_assign: AnnAssignsMap


def calc_maps(proj_info: dict, dirs: PyppDirs) -> Maps:
    return Maps(
        calc_name_map(proj_info, dirs),
        calc_call_map(proj_info, dirs),
        calc_attr_map(proj_info, dirs),
        calc_fn_arg_passed_by_value_map(proj_info, dirs),
        calc_subscriptable_type_map(proj_info, dirs),
        calc_import_map(proj_info, dirs),
        calc_ann_assign_map(proj_info, dirs),
    )
