from dataclasses import dataclass

from src.d_types import CppInclude, QInc


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
    "PyppNpArr": TypeMapInfo("NpArr", [QInc("np_arr.h")]),
}


def lookup_cpp_type(python_type: str, ret_imports: set[CppInclude]) -> str:
    # The way it works is that whenever you looked up the type, it automatically
    # is added to the ret_imports
    if python_type not in TYPES_MAP:
        return python_type
    val = TYPES_MAP[python_type]
    for include in val.includes:
        ret_imports.add(include)
    return val.val
