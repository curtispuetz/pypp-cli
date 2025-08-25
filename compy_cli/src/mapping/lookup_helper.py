from compy_cli.src.deps import Deps
from compy_cli.src.mapping.d_types import (
    ToStringEntry,
    NameOrAttrMap,
)
from compy_cli.src.mapping.util import find_map_info


def lookup_helper(key: str, d: Deps, map: NameOrAttrMap) -> ToStringEntry | None:
    if key not in map:
        return None
    map_info = find_map_info(map[key], d)
    if map_info is None:
        return None
    d.add_incs(map_info.includes)
    return map_info
