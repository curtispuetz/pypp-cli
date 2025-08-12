from pypp_core.src.util.inner_strings import calc_inside_rd

FN_ARG_PASSED_BY_VALUE: set[str] = {
    "int",
    "double",  # python float
    "bool",
    "float",  # python float32
    "int8_t",
    "int16_t",
    "int32_t",
    "int64_t",
    "uint8_t",
    "uint16_t",
    "uint32_t",
    "uint64_t",
}


def lookup_cpp_fn_arg(cpp_arg_type: str) -> str:
    is_pass_by_ref, cpp_arg_type = _is_pass_by_ref(cpp_arg_type)
    if cpp_arg_type in FN_ARG_PASSED_BY_VALUE:
        return cpp_arg_type
    pass_by_ref_str = "&" if is_pass_by_ref else ""
    before_and_after = cpp_arg_type.split("<", 1)
    if len(before_and_after) == 1:
        return f"{before_and_after[0]}{pass_by_ref_str}"
    before, after = before_and_after
    return f"{before}<{after}{pass_by_ref_str}"


def _is_pass_by_ref(cpp_arg_type: str) -> tuple[bool, str]:
    ret: bool = True
    if cpp_arg_type.startswith("Valu(") and cpp_arg_type.endswith(")"):
        cpp_arg_type = calc_inside_rd(cpp_arg_type)
        ret = False
    return ret, cpp_arg_type
