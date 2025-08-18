from pypp_core.src.deps import Deps
from pypp_core.src.mapping.info_types import (
    NamesCallsOrAttrsMap,
    NamesCallsOrAttrsMapInfo,
)


def lookup_helper(
    key: str, d: Deps, map: NamesCallsOrAttrsMap
) -> NamesCallsOrAttrsMapInfo | None:
    if key not in map:
        return None
    val = map[key]
    if val.required_import is not None and not d.is_imported(val.required_import):
        return None
    for include in val.includes:
        d.add_inc(include)
    return val
