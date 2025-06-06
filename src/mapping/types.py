from dataclasses import dataclass

from src.d_types import CppInclude, SBInc


@dataclass(frozen=True, slots=True)
class _FnArg:
    const: bool
    reference: bool


_D = tuple[str, list[CppInclude], _FnArg]

TYPES_MAP: dict[str, _D] = {
    "str": ("std::string", [SBInc("string")], _FnArg(True, True)),
    "int": ("int", [], _FnArg(False, False)),
}


def lookup_cpp_type(python_type: str, ret_imports: set[CppInclude]) -> str:
    # The way it works is that whenever you looked up the type, it automatically
    # is added to the ret_imports
    val = _lookup_cpp_type(python_type, ret_imports)
    if val is None:
        return python_type
    return val[0]


def lookup_cpp_fn_arg(python_type: str, ret_imports: set[CppInclude]) -> str:
    val = _lookup_cpp_type(python_type, ret_imports)
    if val is None:
        return python_type  # NOTE: or, should always references be passed?
    ret = val[0]
    if val[2].const:
        ret = "const " + ret
    if val[2].reference:
        ret += "&"
    return ret


def _lookup_cpp_type(python_type: str, ret_imports: set[CppInclude]) -> _D | None:
    if python_type not in TYPES_MAP:
        return None
    val = TYPES_MAP[python_type]
    for include in val[1]:
        ret_imports.add(include)
    return val
