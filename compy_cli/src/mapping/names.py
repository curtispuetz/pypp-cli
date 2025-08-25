from compy_cli.src.deps import Deps
from compy_cli.src.mapping.info_types import ToStringEntry
from compy_cli.src.mapping.lookup_helper import lookup_helper


def lookup_cpp_name(name: str, d: Deps) -> str:
    val = lookup_helper(name, d, d.maps.name)
    if val is None:
        return name
    assert isinstance(val, ToStringEntry), "shouldn't happen"
    return val.to
