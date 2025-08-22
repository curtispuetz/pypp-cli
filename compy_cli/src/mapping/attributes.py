from compy_cli.src.deps import Deps
from compy_cli.src.mapping.info_types import MapInfo
from compy_cli.src.mapping.lookup_helper import lookup_helper


def lookup_cpp_attribute(attr: str, d: Deps):
    val = lookup_helper(attr, d, d.maps.attr)
    if val is None:
        return attr
    assert isinstance(val, MapInfo), "shouldn't happen"
    return val.val
