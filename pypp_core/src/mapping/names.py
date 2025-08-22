from pypp_core.src.deps import Deps
from pypp_core.src.mapping.info_types import MapInfo
from pypp_core.src.mapping.lookup_helper import lookup_helper


def lookup_cpp_name(name: str, d: Deps) -> str:
    val = lookup_helper(name, d, d.maps.name)
    if val is None:
        return name
    assert isinstance(val, MapInfo), "shouldn't happen"
    return val.val
