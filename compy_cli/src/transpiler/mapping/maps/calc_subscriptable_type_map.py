from compy_cli.src.compy_dirs import CompyDirs
from compy_cli.src.transpiler.d_types import PySpecificImpFrom
from compy_cli.src.transpiler.util.load_proj_info import ProjInfo
from compy_cli.src.transpiler.mapping.d_types import SubscriptableTypeMap
from compy_cli.src.transpiler.mapping.maps.util.calc_map_2 import calc_map_2

SUBSCRIPTABLE_TYPE_MAP: SubscriptableTypeMap = {
    "PyList": {None},
    "PyDict": {None},
    "PyTup": {None},
    "PySet": {None},
    "PyDefaultDict": {PySpecificImpFrom("collections", "defaultdict")},
    "Uni": {PySpecificImpFrom("compy_python.union", "Uni")},
}


def _warning_msg(installed_library: str, full_type_str: str) -> str:
    return (
        f"Compy transpiler already considers {full_type_str} a subscriptable type. "
        f"Library {installed_library} is potentially changing this behavior."
    )


def calc_subscriptable_type_map(
    proj_info: ProjInfo, dirs: CompyDirs
) -> SubscriptableTypeMap:
    return calc_map_2(
        SUBSCRIPTABLE_TYPE_MAP,
        proj_info,
        dirs,
        "subscriptable_types",
        _warning_msg,
    )
