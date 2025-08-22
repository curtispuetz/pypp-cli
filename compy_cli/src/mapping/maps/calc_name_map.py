from functools import partial

from compy_cli.src.compy_dirs import CompyDirs
from compy_cli.src.d_types import (
    PySpecificImpFrom,
    AngInc,
    QInc,
)
from compy_cli.src.mapping.maps.util import (
    calc_map_info,
    load_map,
    calc_common_warning_msg,
)
from compy_cli.src.mapping.info_types import MapInfo, NameMap


NAME_MAP: NameMap = {
    "str": {None: MapInfo("PyStr", [QInc("py_str.h")])},
    # NOTE: technically I don't think this is necessary since int and int are the same
    "int": {None: MapInfo("int", [])},
    "float": {None: MapInfo("double", [])},
    "float32": {
        PySpecificImpFrom("compy_python.custom_types", "float32"): MapInfo("float", [])
    },
    "int8_t": {
        PySpecificImpFrom("compy_python.custom_types", "int8_t"): MapInfo(
            "int8_t",
            [AngInc("cstdint")],
        )
    },
    "int16_t": {
        PySpecificImpFrom("compy_python.custom_types", "int16_t"): MapInfo(
            "int16_t",
            [AngInc("cstdint")],
        )
    },
    "int32_t": {
        PySpecificImpFrom("compy_python.custom_types", "int32_t"): MapInfo(
            "int32_t",
            [AngInc("cstdint")],
        )
    },
    "int64_t": {
        PySpecificImpFrom("compy_python.custom_types", "int64_t"): MapInfo(
            "int64_t",
            [AngInc("cstdint")],
        )
    },
    "uint8_t": {
        PySpecificImpFrom("compy_python.custom_types", "uint8_t"): MapInfo(
            "uint8_t", [AngInc("cstdint")]
        )
    },
    "uint16_t": {
        PySpecificImpFrom("compy_python.custom_types", "uint16_t"): MapInfo(
            "uint16_t", [AngInc("cstdint")]
        )
    },
    "uint32_t": {
        PySpecificImpFrom("compy_python.custom_types", "uint32_t"): MapInfo(
            "uint32_t", [AngInc("cstdint")]
        )
    },
    "uint64_t": {
        PySpecificImpFrom("compy_python.custom_types", "uint64_t"): MapInfo(
            "uint64_t", [AngInc("cstdint")]
        )
    },
    "list": {None: MapInfo("PyList", [QInc("py_list.h")])},
    "dict": {None: MapInfo("PyDict", [QInc("py_dict.h")])},
    "defaultdict": {
        PySpecificImpFrom("collections", "defaultdict"): MapInfo(
            "PyDefaultDict", [QInc("py_dict_default.h")]
        )
    },
    "tuple": {None: MapInfo("PyTup", [QInc("py_tuple.h")])},
    "set": {None: MapInfo("PySet", [QInc("py_set.h")])},
    "range": {None: MapInfo("PyRange", [QInc("py_range.h")])},
    "slice": {None: MapInfo("PySlice", [QInc("slice/py_slice.h")])},
    "enumerate": {None: MapInfo("PyEnumerate", [QInc("py_enumerate.h")])},
    "zip": {None: MapInfo("PyZip", [QInc("py_zip.h")])},
    "reversed": {None: MapInfo("PyReversed", [QInc("py_reversed.h")])},
    "Uni": {
        PySpecificImpFrom("compy_python.union", "Uni"): MapInfo(
            "Uni", [QInc("compy_union.h")]
        )
    },
}


def calc_name_map(proj_info: dict, dirs: CompyDirs) -> NameMap:
    return load_map(
        NAME_MAP,
        proj_info,
        dirs,
        "name_map",
        calc_map_info,
        partial(calc_common_warning_msg, name="name"),
    )
