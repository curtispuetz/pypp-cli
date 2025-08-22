from pypp_core.src.deps import Deps
from pypp_core.src.mapping.info_types import (
    MapInfo,
    NameOrAttrMap,
)
from pypp_core.src.mapping.util import find_map_info


def lookup_helper(key: str, d: Deps, map: NameOrAttrMap) -> MapInfo | None:
    if key not in map:
        return None
    map_info = find_map_info(map[key], d)
    if map_info is None:
        return None
    d.add_incs(map_info.includes)
    return map_info
