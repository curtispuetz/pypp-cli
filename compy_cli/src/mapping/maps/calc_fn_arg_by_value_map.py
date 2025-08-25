from compy_cli.src.compy_dirs import CompyDirs
from compy_cli.src.d_types import PySpecificImpFrom
from compy_cli.src.main_scripts.util.load_proj_info import ProjInfo
from compy_cli.src.mapping.d_types import FnArgByValueMap
from compy_cli.src.mapping.maps.util.calc_map_2 import calc_map_2

FN_ARG_PASSED_BY_VALUE_MAP: FnArgByValueMap = {
    "int": {None},
    "double": {None},  # python float
    "bool": {None},
    "float": {
        PySpecificImpFrom("compy_python.custom_types", "float32")
    },  # python float32
    "int8_t": {PySpecificImpFrom("compy_python.custom_types", "int8_t")},
    "int16_t": {PySpecificImpFrom("compy_python.custom_types", "int16_t")},
    "int32_t": {PySpecificImpFrom("compy_python.custom_types", "int32_t")},
    "int64_t": {PySpecificImpFrom("compy_python.custom_types", "int64_t")},
    "uint8_t": {PySpecificImpFrom("compy_python.custom_types", "uint8_t")},
    "uint16_t": {PySpecificImpFrom("compy_python.custom_types", "uint16_t")},
    "uint32_t": {PySpecificImpFrom("compy_python.custom_types", "uint32_t")},
    "uint64_t": {PySpecificImpFrom("compy_python.custom_types", "uint64_t")},
    "PyRange": {None},
}


def _warning_msg(installed_library: str, full_type_str: str) -> str:
    return (
        f"Compy transpiler already passes the type {full_type_str} by value always. "
        f"Library {installed_library} is potentially changing this behavior."
    )


def calc_fn_arg_passed_by_value_map(
    proj_info: ProjInfo, dirs: CompyDirs
) -> FnArgByValueMap:
    return calc_map_2(
        FN_ARG_PASSED_BY_VALUE_MAP,
        proj_info,
        dirs,
        "always_pass_by_value",
        _warning_msg,
    )
