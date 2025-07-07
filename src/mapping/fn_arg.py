FN_ARG_PASSED_BY_VALUE: set[str] = {
    "int",
    "bool",
    # Is float even supported in pypp? Maybe it is through np.float32 values?
    "float",
    "double",
    "PyRange",
}


def lookup_cpp_fn_arg(cpp_arg: str, is_pass_by_ref: bool) -> str:
    if cpp_arg in FN_ARG_PASSED_BY_VALUE:
        return cpp_arg
    pass_by_ref_str = "&" if is_pass_by_ref else ""
    before_and_after = cpp_arg.split("<", 1)
    if len(before_and_after) == 1:
        return f"{before_and_after[0]}{pass_by_ref_str}"
    before, after = before_and_after
    return f"{before}<{after}{pass_by_ref_str}"
