from pypp_core.src.pypp_dirs import PyppDirs
from pypp_core.src.d_types import PySpecificImpFrom
from pypp_core.src.mapping.info_types import SubscriptableTypeMap
from pypp_core.src.mapping.maps.util import load_map

SUBSCRIPTABLE_TYPE_MAP: SubscriptableTypeMap = {
    "PyList": {None: None},
    "PyDict": {None: None},
    "PyTup": {None: None},
    "PySet": {None: None},
    "PyDefaultDict": {PySpecificImpFrom("collections", "defaultdict"): None},
    "Uni": {PySpecificImpFrom("pypp_python.union", "Uni"): None},
}


def _warning_msg(installed_library: str, full_type_str: str) -> str:
    return (
        f"Py++ transpiler already considers {full_type_str} a subscriptable type. "
        f"Library {installed_library} is potentially changing this behavior."
    )


def calc_subscriptable_type_map(
    proj_info: dict, dirs: PyppDirs
) -> SubscriptableTypeMap:
    return load_map(
        SUBSCRIPTABLE_TYPE_MAP,
        proj_info,
        dirs,
        "subscriptable_types",
        lambda _a, _b: None,
        _warning_msg,
    )
