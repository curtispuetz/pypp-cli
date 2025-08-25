from compy_cli.src.compy_dirs import CompyDirs
from compy_cli.src.d_types import PySpecificImpFrom
from compy_cli.src.main_scripts.util.load_proj_info import ProjInfo
from compy_cli.src.mapping.info_types import SubscriptableTypeMap
from compy_cli.src.mapping.maps.util import load_map

SUBSCRIPTABLE_TYPE_MAP: SubscriptableTypeMap = {
    "PyList": {None: None},
    "PyDict": {None: None},
    "PyTup": {None: None},
    "PySet": {None: None},
    "PyDefaultDict": {PySpecificImpFrom("collections", "defaultdict"): None},
    "Uni": {PySpecificImpFrom("compy_python.union", "Uni"): None},
}


def _warning_msg(installed_library: str, full_type_str: str) -> str:
    return (
        f"Compy transpiler already considers {full_type_str} a subscriptable type. "
        f"Library {installed_library} is potentially changing this behavior."
    )


def calc_subscriptable_type_map(
    proj_info: ProjInfo, dirs: CompyDirs
) -> SubscriptableTypeMap:
    return load_map(
        SUBSCRIPTABLE_TYPE_MAP,
        proj_info,
        dirs,
        "subscriptable_types",
        lambda _a, _b: None,
        _warning_msg,
    )
