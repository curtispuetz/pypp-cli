from dataclasses import dataclass

from src.d_types import CppInclude, QInc
from src.util.ret_imports import RetImports, add_inc


@dataclass(frozen=True, slots=True)
class TypeMapInfo:
    val: str
    includes: list[CppInclude]


TYPES_MAP: dict[str, TypeMapInfo] = {
    "str": TypeMapInfo("PyStr", [QInc("py_str.h")]),
    # NOTE: technically I don't think this is necessary since int and int are the same
    "int": TypeMapInfo("int", []),
    "float": TypeMapInfo("double", []),
    "list": TypeMapInfo("PyList", [QInc("py_list.h")]),
    "dict": TypeMapInfo("PyDict", [QInc("py_dict.h")]),
    "tuple": TypeMapInfo("PyTup", [QInc("py_tuple.h")]),
    "set": TypeMapInfo("PySet", [QInc("py_set.h")]),
    "range": TypeMapInfo("PyRange", [QInc("py_range.h")]),
    "slice": TypeMapInfo("PySlice", [QInc("py_slice.h")]),
    "enumerate": TypeMapInfo("PyEnumerate", [QInc("py_enumerate.h")]),
    "PyppNpArr": TypeMapInfo("NpArr", [QInc("np_arr.h")]),
}


def lookup_cpp_type(
    python_type: str,
    ret_imports: RetImports,
    include_in_header: bool = False,
) -> str:
    # The way it works is that whenever you looked up the type, it automatically
    # is added to the ret_imports
    if python_type not in TYPES_MAP:
        return python_type
    val = TYPES_MAP[python_type]
    for include in val.includes:
        add_inc(ret_imports, include, include_in_header)
    return val.val
