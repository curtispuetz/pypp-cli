from compy_cli.src.transpilers.other.module.d_types import (
    PySpecificImpFrom,
    AngInc,
    QInc,
)
from compy_cli.src.transpilers.other.maps.d_types import (
    ToStringEntry,
    NameMap,
)


NAME_MAP: NameMap = {
    "str": {None: ToStringEntry("PyStr", [QInc("py_str.h")])},
    # NOTE: technically I don't think this is necessary since int and int are the same
    "int": {None: ToStringEntry("int", [])},
    "float": {None: ToStringEntry("double", [])},
    "float32": {
        PySpecificImpFrom("compy_python.custom_types", "float32"): ToStringEntry(
            "float", []
        )
    },
    "int8_t": {
        PySpecificImpFrom("compy_python.custom_types", "int8_t"): ToStringEntry(
            "int8_t",
            [AngInc("cstdint")],
        )
    },
    "int16_t": {
        PySpecificImpFrom("compy_python.custom_types", "int16_t"): ToStringEntry(
            "int16_t",
            [AngInc("cstdint")],
        )
    },
    "int32_t": {
        PySpecificImpFrom("compy_python.custom_types", "int32_t"): ToStringEntry(
            "int32_t",
            [AngInc("cstdint")],
        )
    },
    "int64_t": {
        PySpecificImpFrom("compy_python.custom_types", "int64_t"): ToStringEntry(
            "int64_t",
            [AngInc("cstdint")],
        )
    },
    "uint8_t": {
        PySpecificImpFrom("compy_python.custom_types", "uint8_t"): ToStringEntry(
            "uint8_t", [AngInc("cstdint")]
        )
    },
    "uint16_t": {
        PySpecificImpFrom("compy_python.custom_types", "uint16_t"): ToStringEntry(
            "uint16_t", [AngInc("cstdint")]
        )
    },
    "uint32_t": {
        PySpecificImpFrom("compy_python.custom_types", "uint32_t"): ToStringEntry(
            "uint32_t", [AngInc("cstdint")]
        )
    },
    "uint64_t": {
        PySpecificImpFrom("compy_python.custom_types", "uint64_t"): ToStringEntry(
            "uint64_t", [AngInc("cstdint")]
        )
    },
    "list": {None: ToStringEntry("PyList", [QInc("py_list.h")])},
    "dict": {None: ToStringEntry("PyDict", [QInc("py_dict.h")])},
    "defaultdict": {
        PySpecificImpFrom("collections", "defaultdict"): ToStringEntry(
            "PyDefaultDict", [QInc("py_dict_default.h")]
        )
    },
    "tuple": {None: ToStringEntry("PyTup", [QInc("py_tuple.h")])},
    "set": {None: ToStringEntry("PySet", [QInc("py_set.h")])},
    "range": {None: ToStringEntry("PyRange", [QInc("py_range.h")])},
    "slice": {None: ToStringEntry("PySlice", [QInc("slice/py_slice.h")])},
    "enumerate": {None: ToStringEntry("PyEnumerate", [QInc("py_enumerate.h")])},
    "zip": {None: ToStringEntry("PyZip", [QInc("py_zip.h")])},
    "reversed": {None: ToStringEntry("PyReversed", [QInc("py_reversed.h")])},
    "Uni": {
        PySpecificImpFrom("compy_python.union", "Uni"): ToStringEntry(
            "Uni", [QInc("compy_union.h")]
        )
    },
}
