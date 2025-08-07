from dataclasses import dataclass

from pypp_core.src.d_types import (
    CppInclude,
    QInc,
    AngInc,
    PySpecificImport,
    PySpecificImpFrom,
)
from pypp_core.src.deps import Deps


@dataclass(frozen=True, slots=True)
class _TypeMapInfo:
    val: str
    includes: list[CppInclude]
    required_import: PySpecificImport | None = None


# TODO: for bridge library creation, users can define their types for here
TYPES_MAP: dict[str, _TypeMapInfo] = {
    "str": _TypeMapInfo("PyStr", [QInc("py_str.h")]),
    # NOTE: technically I don't think this is necessary since int and int are the same
    "int": _TypeMapInfo("int", []),
    "float": _TypeMapInfo("double", []),
    "float32": _TypeMapInfo(
        "float", [], PySpecificImpFrom("pypp_python.custom_types", "float32")
    ),
    "int8_t": _TypeMapInfo(
        "int8_t",
        [AngInc("cstdint")],
        PySpecificImpFrom("pypp_python.custom_types", "int8_t"),
    ),
    "int16_t": _TypeMapInfo(
        "int16_t",
        [AngInc("cstdint")],
        PySpecificImpFrom("pypp_python.custom_types", "int16_t"),
    ),
    "int32_t": _TypeMapInfo(
        "int32_t",
        [AngInc("cstdint")],
        PySpecificImpFrom("pypp_python.custom_types", "int32_t"),
    ),
    "int64_t": _TypeMapInfo(
        "int64_t",
        [AngInc("cstdint")],
        PySpecificImpFrom("pypp_python.custom_types", "int64_t"),
    ),
    "uint8_t": _TypeMapInfo(
        "uint8_t",
        [AngInc("cstdint")],
        PySpecificImpFrom("pypp_python.custom_types", "uint8_t"),
    ),
    "uint16_t": _TypeMapInfo(
        "uint16_t",
        [AngInc("cstdint")],
        PySpecificImpFrom("pypp_python.custom_types", "uint16_t"),
    ),
    "uint32_t": _TypeMapInfo(
        "uint32_t",
        [AngInc("cstdint")],
        PySpecificImpFrom("pypp_python.custom_types", "uint32_t"),
    ),
    "uint64_t": _TypeMapInfo(
        "uint64_t",
        [AngInc("cstdint")],
        PySpecificImpFrom("pypp_python.custom_types", "uint64_t"),
    ),
    "list": _TypeMapInfo("PyList", [QInc("py_list.h")]),
    "dict": _TypeMapInfo("PyDict", [QInc("py_dict.h")]),
    "defaultdict": _TypeMapInfo(
        "PyDefaultDict",
        [QInc("py_dict_default.h")],
        PySpecificImpFrom("collections", "defaultdict"),
    ),
    "tuple": _TypeMapInfo("PyTup", [QInc("py_tuple.h")]),
    "set": _TypeMapInfo("PySet", [QInc("py_set.h")]),
    "range": _TypeMapInfo("PyRange", [QInc("py_range.h")]),
    "slice": _TypeMapInfo("PySlice", [QInc("slice/py_slice.h")]),
    "enumerate": _TypeMapInfo("PyEnumerate", [QInc("py_enumerate.h")]),
    "zip": _TypeMapInfo("PyZip", [QInc("py_zip.h")]),
    "reversed": _TypeMapInfo("PyReversed", [QInc("py_reversed.h")]),
    "Uni": _TypeMapInfo(
        "Uni", [QInc("pypp_union.h")], PySpecificImpFrom("pypp_python.union", "Uni")
    ),
}


def lookup_cpp_type(
    python_type: str,
    d: Deps,
    include_in_header: bool = False,
) -> str:
    # The way it works is that whenever you looked up the type, it automatically
    # is added to the ret_imports
    if python_type not in TYPES_MAP:
        return python_type
    val = TYPES_MAP[python_type]
    if val.required_import is not None and not d.is_imported(val.required_import):
        return python_type
    for include in val.includes:
        d.add_inc(include, include_in_header)
    return val.val
