from dataclasses import dataclass

from src.d_types import CppInclude, QInc, AngInc
from src.deps import Deps


@dataclass(frozen=True, slots=True)
class TypeMapInfo:
    val: str
    includes: list[CppInclude]


TYPES_MAP: dict[str, TypeMapInfo] = {
    "str": TypeMapInfo("PyStr", [QInc("py_str.h")]),
    # NOTE: technically I don't think this is necessary since int and int are the same
    "int": TypeMapInfo("int", []),
    "float": TypeMapInfo("double", []),
    "float32": TypeMapInfo("float", []),
    "int8_t": TypeMapInfo("int8_t", [AngInc("cstdint")]),
    "int16_t": TypeMapInfo("int16_t", [AngInc("cstdint")]),
    "int32_t": TypeMapInfo("int32_t", [AngInc("cstdint")]),
    "int64_t": TypeMapInfo("int64_t", [AngInc("cstdint")]),
    "uint8_t": TypeMapInfo("uint8_t", [AngInc("cstdint")]),
    "uint16_t": TypeMapInfo("uint16_t", [AngInc("cstdint")]),
    "uint32_t": TypeMapInfo("uint32_t", [AngInc("cstdint")]),
    "uint64_t": TypeMapInfo("uint64_t", [AngInc("cstdint")]),
    "list": TypeMapInfo("PyList", [QInc("py_list.h")]),
    "dict": TypeMapInfo("PyDict", [QInc("py_dict.h")]),
    "defaultdict": TypeMapInfo("PyDefaultDict", [QInc("py_dict_default.h")]),
    "tuple": TypeMapInfo("PyTup", [QInc("py_tuple.h")]),
    "set": TypeMapInfo("PySet", [QInc("py_set.h")]),
    "range": TypeMapInfo("PyRange", [QInc("py_range.h")]),
    "slice": TypeMapInfo("PySlice", [QInc("slice/py_slice.h")]),
    "enumerate": TypeMapInfo("PyEnumerate", [QInc("py_enumerate.h")]),
    "zip": TypeMapInfo("PyZip", [QInc("py_zip.h")]),
    "reversed": TypeMapInfo("PyReversed", [QInc("py_reversed.h")]),
    "Uni": TypeMapInfo("Uni", [QInc("pypp_union.h")]),
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
    for include in val.includes:
        d.add_inc(include, include_in_header)
    return val.val
