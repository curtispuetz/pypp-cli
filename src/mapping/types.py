from dataclasses import dataclass

from src.d_types import CppInclude, SBInc, QInc


@dataclass(frozen=True, slots=True)
class FnArgInfo:
    const: bool
    reference: bool


@dataclass(frozen=True, slots=True)
class TypeMapInfo:
    val: str
    other_ann_assign: bool
    includes: list[CppInclude]
    fn_arg_info: FnArgInfo


TYPES_MAP: dict[str, TypeMapInfo] = {
    "str": TypeMapInfo("PyStr", True, [QInc("py_str.h")], FnArgInfo(True, True)),
    "int": TypeMapInfo("int", False, [], FnArgInfo(False, False)),
    # TODO: test the vector as a function argument
    "list": TypeMapInfo("std::vector", False, [SBInc("vector")], FnArgInfo(True, True)),
}


def lookup_cpp_type(python_type: str, ret_imports: set[CppInclude]) -> str:
    # The way it works is that whenever you looked up the type, it automatically
    # is added to the ret_imports
    val = lookup_cpp_type_info(python_type, ret_imports)
    if val is None:
        return python_type
    return val.val


def lookup_cpp_fn_arg(python_type: str, ret_imports: set[CppInclude]) -> str:
    val = lookup_cpp_type_info(python_type, ret_imports)
    if val is None:
        return python_type  # NOTE: or, should always references be passed?
    ret = val.val
    if val.fn_arg_info.const:
        ret = "const " + ret
    if val.fn_arg_info.reference:
        ret += "&"
    return ret


def lookup_cpp_subscript_value_type(
    python_type: str, ret_imports: set[CppInclude]
) -> tuple[str, str]:
    val = lookup_cpp_type_info(python_type, ret_imports)
    if val is None:
        return python_type + "[", "]"
    return val.val + "<", ">"  # Note: will it always be square brackets


def lookup_cpp_type_info(
    python_type: str, ret_imports: set[CppInclude]
) -> TypeMapInfo | None:
    if python_type not in TYPES_MAP:
        return None
    val = TYPES_MAP[python_type]
    for include in val.includes:
        ret_imports.add(include)
    return val
