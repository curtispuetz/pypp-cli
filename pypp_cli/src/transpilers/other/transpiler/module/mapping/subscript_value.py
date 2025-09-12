from pypp_cli.src.transpilers.other.transpiler.deps import Deps
from pypp_cli.src.transpilers.other.transpiler.module.mapping.util import is_map_entry


def lookup_cpp_subscript_value_type(cpp_value: str, d: Deps) -> tuple[str, str]:
    if cpp_value in d.maps.subscriptable_type:
        if is_map_entry(d.maps.subscriptable_type[cpp_value], d):
            return cpp_value + "<", ">"
    return cpp_value + "[", "]"
