from compy_cli.src.transpilers.other.module.d_types import PySpecificImpFrom
from compy_cli.src.transpilers.other.maps.d_types import SubscriptableTypeMap

SUBSCRIPTABLE_TYPE_MAP: SubscriptableTypeMap = {
    "PyList": {None},
    "PyDict": {None},
    "PyTup": {None},
    "PySet": {None},
    "PyDefaultDict": {PySpecificImpFrom("collections", "defaultdict")},
    "Uni": {PySpecificImpFrom("compy_python.union", "Uni")},
}


def subscriptable_type_warning_msg(installed_library: str, full_type_str: str) -> str:
    return (
        f"Compy transpiler already considers {full_type_str} a subscriptable type. "
        f"Library {installed_library} is potentially changing this behavior."
    )
