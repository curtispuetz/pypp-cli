from compy_cli.src.compy_dirs import CompyDirs
from compy_cli.src.d_types import PySpecificImpFrom
from compy_cli.src.mapping.info_types import FnArgByValueMap
from compy_cli.src.mapping.maps.util import load_map

FN_ARG_PASSED_BY_VALUE_MAP: FnArgByValueMap = {
    "int": {None: None},
    "double": {None: None},  # python float
    "bool": {None: None},
    "float": {
        PySpecificImpFrom("compy_python.custom_types", "float32"): None
    },  # python float32
    "int8_t": {PySpecificImpFrom("compy_python.custom_types", "int8_t"): None},
    "int16_t": {PySpecificImpFrom("compy_python.custom_types", "int16_t"): None},
    "int32_t": {PySpecificImpFrom("compy_python.custom_types", "int32_t"): None},
    "int64_t": {PySpecificImpFrom("compy_python.custom_types", "int64_t"): None},
    "uint8_t": {PySpecificImpFrom("compy_python.custom_types", "uint8_t"): None},
    "uint16_t": {PySpecificImpFrom("compy_python.custom_types", "uint16_t"): None},
    "uint32_t": {PySpecificImpFrom("compy_python.custom_types", "uint32_t"): None},
    "uint64_t": {PySpecificImpFrom("compy_python.custom_types", "uint64_t"): None},
    "PyRange": {None: None},
}


def _warning_msg(installed_library: str, full_type_str: str) -> str:
    return (
        f"Py++ transpiler already passes the type {full_type_str} by value always. "
        f"Library {installed_library} is potentially changing this behavior."
    )


def calc_fn_arg_passed_by_value_map(
    proj_info: dict, dirs: CompyDirs
) -> FnArgByValueMap:
    return load_map(
        FN_ARG_PASSED_BY_VALUE_MAP,
        proj_info,
        dirs,
        "always_pass_by_value",
        lambda _a, _b: None,
        _warning_msg,
    )
