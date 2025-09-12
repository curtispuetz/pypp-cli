from pypp_cli.src.transpilers.other.transpiler.deps import Deps
from pypp_cli.src.transpilers.other.transpiler.maps.fn_arg_passed_by_value import (
    PRIMITIVE_TYPES,
)


def is_primitive_type(type_cpp: str, d: Deps) -> bool:
    for k, v in PRIMITIVE_TYPES.items():
        if type_cpp == k:
            for imp in v:
                if imp is None:
                    return True
                if d.is_imported(imp):
                    return True
    return False
