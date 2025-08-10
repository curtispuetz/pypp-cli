from pypp_core.src.deps import Deps


def lookup_cpp_call(
    call: str,
    d: Deps,
    include_in_header: bool,
) -> tuple[str, str]:
    if call not in d.maps.calls:
        return call + "(", ")"
    val = d.maps.calls[call]
    if val.required_import is not None and not d.is_imported(val.required_import):
        return call + "(", ")"
    for include in val.includes:
        d.add_inc(include, include_in_header)
    return val.left, val.right
