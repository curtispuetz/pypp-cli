from dataclasses import dataclass

from pypp_core.src.config import PyppDirs
from pypp_core.src.mapping.maps.calc_attrs_map import calc_attrs_map
from pypp_core.src.mapping.maps.calc_calls_map import calc_calls_map
from pypp_core.src.mapping.maps.calc_names_map import calc_names_map
from pypp_core.src.mapping.util import MapInfo, CallMapInfo


@dataclass(frozen=True, slots=True)
class Maps:
    names: dict[str, MapInfo]
    calls: dict[str, CallMapInfo]
    attrs: dict[str, MapInfo]


def calc_maps(project_info: dict, dirs: PyppDirs) -> Maps:
    return Maps(
        calc_names_map(project_info, dirs),
        calc_calls_map(project_info, dirs),
        calc_attrs_map(project_info, dirs),
    )
