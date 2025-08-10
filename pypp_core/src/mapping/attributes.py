from pypp_core.src.d_types import PyImport, QInc
from pypp_core.src.deps import Deps
from pypp_core.src.mapping.util import MapInfo

# TODO: for bridge library creation, users can define their types for here

ATTR_MAP: dict[str, MapInfo] = {
    "random.Random": MapInfo(
        "random::Random",
        [QInc("pypp_random.h")],
        PyImport("random"),
    )
}


def lookup_cpp_attribute(attr: str, d: Deps, include_in_header: bool = False):
    if attr not in ATTR_MAP:
        return attr
    val = ATTR_MAP[attr]
    if val.required_import is not None and not d.is_imported(val.required_import):
        return attr
    for include in val.includes:
        d.add_inc(include, include_in_header)
    return val.val
