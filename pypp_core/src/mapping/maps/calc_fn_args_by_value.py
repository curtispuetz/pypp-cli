from pypp_core.src.config import PyppDirs
from pypp_core.src.d_types import PySpecificImport, PySpecificImpFrom
from pypp_core.src.mapping.maps.util import (
    load_map,
    calc_specific_imports,
)

FN_ARG_PASSED_BY_VALUE: dict[str, PySpecificImport | None] = {
    "int": None,
    "double": None,  # python float
    "bool": None,
    "float": PySpecificImpFrom("pypp_python.custom_types", "float32"),  # python float32
    "int8_t": PySpecificImpFrom("pypp_python.custom_types", "int8_t"),
    "int16_t": PySpecificImpFrom("pypp_python.custom_types", "int16_t"),
    "int32_t": PySpecificImpFrom("pypp_python.custom_types", "int32_t"),
    "int64_t": PySpecificImpFrom("pypp_python.custom_types", "int64_t"),
    "uint8_t": PySpecificImpFrom("pypp_python.custom_types", "uint8_t"),
    "uint16_t": PySpecificImpFrom("pypp_python.custom_types", "uint16_t"),
    "uint32_t": PySpecificImpFrom("pypp_python.custom_types", "uint32_t"),
    "uint64_t": PySpecificImpFrom("pypp_python.custom_types", "uint64_t"),
    "PyRange": None,
}


def _warning_msg(installed_library: str, _type: str) -> str:
    return (
        f"Py++ transpiler already passes the type {_type} by value always. "
        f"Library {installed_library} is potentially changing this behavior."
    )


def calc_fn_args_passed_by_value(
    proj_info: dict, dirs: PyppDirs
) -> dict[str, PySpecificImport | None]:
    return load_map(
        FN_ARG_PASSED_BY_VALUE,
        proj_info,
        dirs,
        "always_pass_by_value",
        calc_specific_imports,
        _warning_msg,
    )
