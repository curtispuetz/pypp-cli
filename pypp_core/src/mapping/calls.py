from pypp_core.src.deps import Deps
from pypp_core.src.mapping.info_types import CallMapInfo
from pypp_core.src.mapping.lookup_helper import lookup_helper


def lookup_cpp_call(call: str, d: Deps) -> tuple[str, str]:
    val = lookup_helper(call, d, d.maps.calls)
    if val is None:
        return call + "(", ")"
    assert isinstance(val, CallMapInfo), "shouldn't happen"
    return val.left, val.right
