from pathlib import Path
from compy_cli.src.transpiler.module.d_types import PySpecificImpFrom
from compy_cli.src.transpiler.maps.d_types import SubscriptableTypeMap
from compy_cli.src.transpiler.maps.util.calc_map_2 import calc_map_2

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
    installed_bridge_libs: dict[str, str], py_env_parent_dir: Path
) -> SubscriptableTypeMap:
    return calc_map_2(
        SUBSCRIPTABLE_TYPE_MAP,
        installed_bridge_libs,
        py_env_parent_dir,
        "subscriptable_types",
        _warning_msg,
    )
