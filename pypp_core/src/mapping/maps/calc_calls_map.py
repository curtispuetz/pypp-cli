from pypp_core.src.config import PyppDirs
from pypp_core.src.d_types import PySpecificImpFrom, QInc, AngInc
from pypp_core.src.mapping.maps.util import (
    calc_cpp_includes,
    calc_required_py_import,
    load_map,
)
from pypp_core.src.mapping.util import CallMapInfo

CALL_MAP: dict[str, CallMapInfo] = {
    "print": CallMapInfo("print(", ")", [QInc("pypp_util/print.h")]),
    "print_address": CallMapInfo(
        "print(&",
        ")",
        [QInc("pypp_util/print.h")],
        PySpecificImpFrom("pypp_python.printing", "print_address"),
    ),
    "len": CallMapInfo("", ".len()", []),
    "str": CallMapInfo("to_pystr(", ")", [QInc("pypp_util/to_py_str.h")]),
    "range": CallMapInfo("PyRange(", ")", [QInc("py_range.h")]),
    "slice": CallMapInfo("py_slice(", ")", [QInc("slice/creators.h")]),
    "enumerate": CallMapInfo("PyEnumerate(", ")", [QInc("py_enumerate.h")]),
    "reversed": CallMapInfo("PyReversed(", ")", [QInc("py_reversed.h")]),
    "zip": CallMapInfo("PyZip(", ")", [QInc("py_zip.h")]),
    "mov": CallMapInfo(
        "std::move(",
        ")",
        [AngInc("utility")],
        PySpecificImpFrom("pypp_python.ownership", "mov"),
    ),
    "pypp_get_resources": CallMapInfo(
        "pypp_get_resources(",
        ")",
        [QInc("pypp_resources.h")],
        PySpecificImpFrom("pypp_python.resources", "pypp_get_resources"),
    ),
    "int_pow": CallMapInfo(
        "int_pow(",
        ")",
        [QInc("pypp_util/math.h")],
        PySpecificImpFrom("pypp_python.math", "int_pow"),
    ),
}


def calc_calls_map(proj_info: dict, dirs: PyppDirs) -> dict[str, CallMapInfo]:
    return load_map(CALL_MAP, proj_info, dirs, "call", _calc_call_map_info)


def _calc_call_map_info(obj: dict, name: str) -> CallMapInfo:
    assert "left" in obj, f"{name}s_map.json must specify a 'left' for each element"
    assert "right" in obj, f"{name}s_map.json must specify a 'right' for each element"
    cpp_includes = calc_cpp_includes(obj)
    required_import = calc_required_py_import(obj)
    return CallMapInfo(obj["left"], obj["right"], cpp_includes, required_import)
