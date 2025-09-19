from pypp_cli.do.z_i.config import SHOULDNT_HAPPEN
from pypp_cli.do.transpile.transpile.handle.node import Deps
from pypp_cli.do.transpile.transpile.z_i.maps.exceptions import (
    EXCEPTION_NAME_MAP,
)
from pypp_cli.do.transpile.transpile.z_i.maps.d_types import (
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
