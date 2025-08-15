from dataclasses import dataclass

from pypp_core.src.config import PyppDirs
from pypp_core.src.d_types import PySpecificImport
from pypp_core.src.mapping.maps.calc_attrs_map import calc_attrs_map
from pypp_core.src.mapping.maps.calc_calls_map import calc_calls_map
from pypp_core.src.mapping.maps.calc_fn_args_by_value import (
    calc_fn_args_passed_by_value,
)
from pypp_core.src.mapping.maps.calc_names_map import calc_names_map
from pypp_core.src.mapping.info_types import MapInfo, CallMapInfo
from pypp_core.src.mapping.maps.calc_subscriptable_types import calc_subscriptable_types


@dataclass(frozen=True, slots=True)
class Maps:
    names: dict[str, MapInfo]
    calls: dict[str, CallMapInfo]
    attrs: dict[str, MapInfo]
    fn_args_passed_by_value: dict[str, PySpecificImport | None]
    subscriptable_types: dict[str, PySpecificImport | None]


def calc_maps(proj_info: dict, dirs: PyppDirs) -> Maps:
    return Maps(
        calc_names_map(proj_info, dirs),
        calc_calls_map(proj_info, dirs),
        calc_attrs_map(proj_info, dirs),
        calc_fn_args_passed_by_value(proj_info, dirs),
        calc_subscriptable_types(proj_info, dirs),
    )
