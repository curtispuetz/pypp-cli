from pypp_cli.do.transpile.transpile.y.d_types import PySpecificImpFrom
from pypp_cli.do.transpile.transpile.y.maps.d_types import (
    SubscriptableTypeMap,
)
from pypp_cli.y.constants import TRANSPILER_CONFIG_DIR

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
def subscriptable_type_warning_msg(lib: str, full_type_str: str):
    print(
        f"WARNING: Py++ transpiler already considers {full_type_str} a subscriptable "
        f"type. "
        f"Library {lib} is potentially changing this behavior."
    )


def subscriptable_type_warning_msg_local(full_type_str: str):
    print(
        f"WARNING: Py++ transpiler already considers {full_type_str} a subscriptable "
        f"type. "
        f".pypp/{TRANSPILER_CONFIG_DIR}/subscriptable_types.json is potentially "
        f"changing this "
        f"behavior."
    )
