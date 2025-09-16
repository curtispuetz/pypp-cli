from pypp_cli.src.config import SHOULDNT_HAPPEN
from pypp_cli.src.transpilers.library.transpiler.deps import Deps
from pypp_cli.src.transpilers.library.transpiler.maps.call.exceptions import (
    EXCEPTION_NAME_MAP,
)
from pypp_cli.src.transpilers.library.transpiler.maps.d_types import (
    ToStringEntry,
)


def lookup_cpp_exception_type(exception: str, d: Deps) -> str:
    if exception not in EXCEPTION_NAME_MAP:
        return exception
    # Note: will always be none
    data = EXCEPTION_NAME_MAP[exception][None]
    assert isinstance(data, ToStringEntry), SHOULDNT_HAPPEN
    d.add_incs(data.includes)
    return data.to
