from pypp_cli.src.transpilers.other.transpiler.d_types import PySpecificImpFrom
from pypp_cli.src.transpilers.other.transpiler.maps.d_types import FnArgByValueMap

FN_ARG_PASSED_BY_VALUE_MAP: FnArgByValueMap = {
    "int": {None},
    "double": {None},  # python float
    "bool": {None},
    "float": {PySpecificImpFrom("pypp_python", "float32")},  # python float32
    "int8_t": {PySpecificImpFrom("pypp_python", "int8_t")},
    "int16_t": {PySpecificImpFrom("pypp_python", "int16_t")},
    "int32_t": {PySpecificImpFrom("pypp_python", "int32_t")},
    "int64_t": {PySpecificImpFrom("pypp_python", "int64_t")},
    "uint8_t": {PySpecificImpFrom("pypp_python", "uint8_t")},
    "uint16_t": {PySpecificImpFrom("pypp_python", "uint16_t")},
    "uint32_t": {PySpecificImpFrom("pypp_python", "uint32_t")},
    "uint64_t": {PySpecificImpFrom("pypp_python", "uint64_t")},
    "pypp::PyRange": {None},
}


def fn_arg_passed_by_value_warning_msg(
    installed_library: str, full_type_str: str
) -> str:
    return (
        f"Py++ transpiler already passes the type {full_type_str} by value always. "
        f"Library {installed_library} is potentially changing this behavior."
    )
