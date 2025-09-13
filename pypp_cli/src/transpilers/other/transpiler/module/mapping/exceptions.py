from pypp_cli.src.transpilers.other.transpiler.deps import Deps
from pypp_cli.src.transpilers.other.transpiler.maps.call.exceptions import (
    EXCEPTION_NAME_MAP,
)
from pypp_cli.src.transpilers.other.transpiler.maps.d_types import (
    ToStringEntry,
)


def lookup_cpp_exception_type(exception: str, d: Deps) -> str:
    if exception not in EXCEPTION_NAME_MAP:
        return exception
    # Note: will always be none
    data = EXCEPTION_NAME_MAP[exception][None]
    assert isinstance(data, ToStringEntry), "shouldn't happen"
    d.add_incs(data.includes)
    return data.to
