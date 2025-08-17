from pypp_core.src.deps import Deps


def lookup_cpp_subscript_value_type(cpp_value: str, d: Deps) -> tuple[str, str]:
    if cpp_value in d.maps.subscriptable_types:
        r = d.maps.subscriptable_types[cpp_value]
        if r is None or d.is_imported(r):
            return cpp_value + "<", ">"
    return cpp_value + "[", "]"
