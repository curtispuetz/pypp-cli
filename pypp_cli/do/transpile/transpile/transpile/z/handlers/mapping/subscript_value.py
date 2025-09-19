from pypp_cli.do.transpile.transpile.transpile.node import Deps
from pypp_cli.do.transpile.transpile.transpile.z.handlers.mapping.util import (
    is_imported,
)


def lookup_cpp_subscript_value_type(cpp_value: str, d: Deps) -> tuple[str, str]:
    if cpp_value in d.maps.subscriptable_type:
        if is_imported(d.maps.subscriptable_type[cpp_value], d):
            return cpp_value + "<", ">"
    return cpp_value + "[", "]"
