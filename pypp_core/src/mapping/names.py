from pypp_core.src.deps import Deps


def lookup_cpp_name(
    name: str,
    d: Deps,
    include_in_header: bool = False,
) -> str:
    # The way it works is that whenever you looked up the type, it automatically
    # is added to the ret_imports
    if name not in d.maps.names:
        return name
    val = d.maps.names[name]
    if val.required_import is not None and not d.is_imported(val.required_import):
        return name
    for include in val.includes:
        d.add_inc(include, include_in_header)
    return val.val
