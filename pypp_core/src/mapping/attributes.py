from pypp_core.src.deps import Deps

# TODO: DRY
def lookup_cpp_attribute(attr: str, d: Deps, include_in_header: bool = False):
    if attr not in d.maps.attrs:
        return attr
    val = d.maps.attrs[attr]
    if val.required_import is not None and not d.is_imported(val.required_import):
        return attr
    for include in val.includes:
        d.add_inc(include, include_in_header)
    return val.val
