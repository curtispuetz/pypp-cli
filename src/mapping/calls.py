from src.d_types import CppInclude, QInc, AngInc
from src.util.ret_imports import RetImports, add_inc

CALL_MAP: dict[str, tuple[str, str, list[CppInclude]]] = {
    "print": ("print(", ")", [QInc("pypp_util/print.h")]),
    "print_address": ("print(&", ")", [QInc("pypp_util/print.h")]),
    "len": ("", ".len()", []),
    "str": ("to_pystr(", ")", [QInc("pypp_util/to_py_str.h")]),
    "range": ("PyRange(", ")", [QInc("py_range.h")]),
    "slice": ("py_slice(", ")", [QInc("slice/creators.h")]),
    "enumerate": ("PyEnumerate(", ")", [QInc("py_enumerate.h")]),
    "reversed": ("PyReversed(", ")", [QInc("py_reversed.h")]),
    "zip": ("PyZip(", ")", [QInc("py_zip.h")]),
    "mov": ("std::move(", ")", [AngInc("utility")]),
    "pypp_get_resources": ("pypp_get_resources(", ")", [QInc("pypp_resources.h")]),
    "int_pow": ("int_pow(", ")", [QInc("pypp_util/math.h")]),
}


def lookup_cpp_call(
    python_call: str,
    ret_imports: RetImports,
    include_in_header: bool,
) -> tuple[str, str]:
    if python_call not in CALL_MAP:
        return python_call + "(", ")"
    val = CALL_MAP[python_call]
    for include in val[2]:
        add_inc(ret_imports, include, include_in_header)
    return val[0], val[1]
