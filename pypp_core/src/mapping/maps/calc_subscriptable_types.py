from pypp_core.src.config import PyppDirs
from pypp_core.src.d_types import PySpecificImport, PySpecificImpFrom
from pypp_core.src.mapping.maps.util import load_map, calc_specific_imports

SUBSCRIPTABLE_TYPES: dict[str, PySpecificImport | None] = {
    "PyList": None,
    "PyDict": None,
    "PyTup": None,
    "PySet": None,
    "PyDefaultDict": PySpecificImpFrom("collections", "defaultdict"),
    "Uni": PySpecificImpFrom("pypp_python.union", "Uni"),
}


def _warning_msg(installed_library: str, _type: str) -> str:
    return (
        f"Py++ transpiler already considers {_type} a subscriptable type. "
        f"Library {installed_library} is potentially changing this behavior."
    )


def calc_subscriptable_types(
    proj_info: dict, dirs: PyppDirs
) -> dict[str, PySpecificImport | None]:
    return load_map(
        SUBSCRIPTABLE_TYPES,
        proj_info,
        dirs,
        "subscriptable_types",
        calc_specific_imports,
        _warning_msg,
    )
