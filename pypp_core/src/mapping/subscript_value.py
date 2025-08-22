from pypp_core.src.deps import Deps
from pypp_core.src.mapping.info_types import SubscriptableTypeMapValue
from pypp_core.src.mapping.util import is_one


def lookup_cpp_subscript_value_type(cpp_value: str, d: Deps) -> tuple[str, str]:
    if cpp_value in d.maps.subscriptable_types:
        r: SubscriptableTypeMapValue = d.maps.subscriptable_types[cpp_value]
        if is_one(r, d):
            return cpp_value + "<", ">"
    return cpp_value + "[", "]"
