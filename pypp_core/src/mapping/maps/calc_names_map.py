from functools import partial

from pypp_core.src.config import PyppDirs
from pypp_core.src.d_types import (
    PySpecificImpFrom,
    AngInc,
    QInc,
)
from pypp_core.src.mapping.maps.util import (
    calc_map_info,
    load_map,
    calc_common_warning_msg,
)
from pypp_core.src.mapping.info_types import MapInfo


NAMES_MAP: dict[str, MapInfo] = {
    "str": MapInfo("PyStr", [QInc("py_str.h")]),
    # NOTE: technically I don't think this is necessary since int and int are the same
    "int": MapInfo("int", []),
    "float": MapInfo("double", []),
    "float32": MapInfo(
        "float", [], PySpecificImpFrom("pypp_python.custom_types", "float32")
    ),
    "int8_t": MapInfo(
        "int8_t",
        [AngInc("cstdint")],
        PySpecificImpFrom("pypp_python.custom_types", "int8_t"),
    ),
    "int16_t": MapInfo(
        "int16_t",
        [AngInc("cstdint")],
        PySpecificImpFrom("pypp_python.custom_types", "int16_t"),
    ),
    "int32_t": MapInfo(
        "int32_t",
        [AngInc("cstdint")],
        PySpecificImpFrom("pypp_python.custom_types", "int32_t"),
    ),
    "int64_t": MapInfo(
        "int64_t",
        [AngInc("cstdint")],
        PySpecificImpFrom("pypp_python.custom_types", "int64_t"),
    ),
    "uint8_t": MapInfo(
        "uint8_t",
        [AngInc("cstdint")],
        PySpecificImpFrom("pypp_python.custom_types", "uint8_t"),
    ),
    "uint16_t": MapInfo(
        "uint16_t",
        [AngInc("cstdint")],
        PySpecificImpFrom("pypp_python.custom_types", "uint16_t"),
    ),
    "uint32_t": MapInfo(
        "uint32_t",
        [AngInc("cstdint")],
        PySpecificImpFrom("pypp_python.custom_types", "uint32_t"),
    ),
    "uint64_t": MapInfo(
        "uint64_t",
        [AngInc("cstdint")],
        PySpecificImpFrom("pypp_python.custom_types", "uint64_t"),
    ),
    "list": MapInfo("PyList", [QInc("py_list.h")]),
    "dict": MapInfo("PyDict", [QInc("py_dict.h")]),
    "defaultdict": MapInfo(
        "PyDefaultDict",
        [QInc("py_dict_default.h")],
        PySpecificImpFrom("collections", "defaultdict"),
    ),
    "tuple": MapInfo("PyTup", [QInc("py_tuple.h")]),
    "set": MapInfo("PySet", [QInc("py_set.h")]),
    "range": MapInfo("PyRange", [QInc("py_range.h")]),
    "slice": MapInfo("PySlice", [QInc("slice/py_slice.h")]),
    "enumerate": MapInfo("PyEnumerate", [QInc("py_enumerate.h")]),
    "zip": MapInfo("PyZip", [QInc("py_zip.h")]),
    "reversed": MapInfo("PyReversed", [QInc("py_reversed.h")]),
    "Uni": MapInfo(
        "Uni", [QInc("pypp_union.h")], PySpecificImpFrom("pypp_python.union", "Uni")
    ),
}


# TODO: add the PySpecificImport to the maps key. Because otherwise libraries cant have
#  things with the same names.
def calc_names_map(proj_info: dict, dirs: PyppDirs) -> dict[str, MapInfo]:
    return load_map(
        NAMES_MAP,
        proj_info,
        dirs,
        "names_map",
        calc_map_info,
        partial(calc_common_warning_msg, name="name"),
    )
