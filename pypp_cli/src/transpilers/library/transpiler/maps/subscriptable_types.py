from pypp_cli.src.transpilers.library.transpiler.d_types import PySpecificImpFrom
from pypp_cli.src.transpilers.library.transpiler.maps.d_types import (
    SubscriptableTypeMap,
)

SUBSCRIPTABLE_TYPE_MAP: SubscriptableTypeMap = {
    "pypp::PyList": {None},
    "pypp::PyDict": {None},
    "pypp::PyTup": {None},
    "pypp::PySet": {None},
    "pypp::PyDefaultDict": {PySpecificImpFrom("pypp_python", "defaultdict")},
    "pypp::Uni": {PySpecificImpFrom("pypp_python", "Uni")},
}


# TODO later: see if I can just detect this without the configuration. It should be
# possible.
def subscriptable_type_warning_msg(lib: str, full_type_str: str) -> str:
    return (
        f"Py++ transpiler already considers {full_type_str} a subscriptable type. "
        f"Library {lib} is potentially changing this behavior."
    )
