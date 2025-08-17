from pypp_core.src.deps import Deps
from pypp_core.src.mapping.info_types import MapInfo
from pypp_core.src.mapping.lookup_helper import lookup_helper


def lookup_cpp_attribute(attr: str, d: Deps, include_in_header: bool = False):
    val = lookup_helper(attr, d, d.maps.attrs, include_in_header)
    if val is None:
        return attr
    assert isinstance(val, MapInfo), "shouldn't happen"
    return val.val
