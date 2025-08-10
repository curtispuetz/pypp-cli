from typing import TypeVar

from pypp_core.src.deps import Deps

T = TypeVar("T")


def lookup_helper(
    key: str,
    d: Deps,
    map: dict[str, T],
    include_in_header: bool = False,
) -> T | None:
    if key not in map:
        return None
    val = map[key]
    if val.required_import is not None and not d.is_imported(val.required_import):
        return None
    for include in val.includes:
        d.add_inc(include, include_in_header)
    return val
