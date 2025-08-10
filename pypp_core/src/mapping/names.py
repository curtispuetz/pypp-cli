from pypp_core.src.deps import Deps
from pypp_core.src.mapping.lookup_helper import lookup_helper


def lookup_cpp_name(
    name: str,
    d: Deps,
    include_in_header: bool = False,
) -> str:
    val = lookup_helper(name, d, d.maps.names, include_in_header)
    if val is None:
        return name
    return val.val
