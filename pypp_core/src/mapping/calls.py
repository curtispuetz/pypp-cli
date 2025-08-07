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
class _CallMapInfo:
    left: str
    right: str
    includes: list[CppInclude]
    required_import: PySpecificImport | None = None


CALL_MAP: dict[str, _CallMapInfo] = {
    "print": _CallMapInfo("print(", ")", [QInc("pypp_util/print.h")]),
    "print_address": _CallMapInfo(
        "print(&",
        ")",
        [QInc("pypp_util/print.h")],
        PySpecificImpFrom("pypp_python.printing", "print_address"),
    ),
    "len": _CallMapInfo("", ".len()", []),
    "str": _CallMapInfo("to_pystr(", ")", [QInc("pypp_util/to_py_str.h")]),
    "range": _CallMapInfo("PyRange(", ")", [QInc("py_range.h")]),
    "slice": _CallMapInfo("py_slice(", ")", [QInc("slice/creators.h")]),
    "enumerate": _CallMapInfo("PyEnumerate(", ")", [QInc("py_enumerate.h")]),
    "reversed": _CallMapInfo("PyReversed(", ")", [QInc("py_reversed.h")]),
    "zip": _CallMapInfo("PyZip(", ")", [QInc("py_zip.h")]),
    "mov": _CallMapInfo(
        "std::move(",
        ")",
        [AngInc("utility")],
        PySpecificImpFrom("pypp_python.ownership", "mov"),
    ),
    "pypp_get_resources": _CallMapInfo(
        "pypp_get_resources(",
        ")",
        [QInc("pypp_resources.h")],
        PySpecificImpFrom("pypp_python.resources", "pypp_get_resources"),
    ),
    "int_pow": _CallMapInfo(
        "int_pow(",
        ")",
        [QInc("pypp_util/math.h")],
        PySpecificImpFrom("pypp_python.math", "int_pow"),
    ),
}


def lookup_cpp_call(
    python_call: str,
    d: Deps,
    include_in_header: bool,
) -> tuple[str, str]:
    if python_call not in CALL_MAP:
        return python_call + "(", ")"
    val = CALL_MAP[python_call]
    if val.required_import is not None and not d.is_imported(val.required_import):
        return python_call + "(", ")"
    for include in val.includes:
        d.add_inc(include, include_in_header)
    return val.left, val.right
