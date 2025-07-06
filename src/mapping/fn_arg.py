FN_ARG_PASSED_BY_VALUE: set[str] = {
    "int",
    "bool",
    # Is float even supported in pypp? Maybe it is through np.float32 values?
    "float",
    "double",
    "PyRange",
}

# TODO: remove all usages of const. Py++ won't have const for now.
def lookup_cpp_fn_arg(cpp_arg: str, is_const: bool) -> str:
    if cpp_arg in FN_ARG_PASSED_BY_VALUE:
        return cpp_arg
    const_str = "const " if is_const else ""
    before_and_after = cpp_arg.split("<", 1)
    if len(before_and_after) == 1:
        return f"{const_str}{before_and_after[0]}&"
    before, after = before_and_after
    return f"{const_str}{before}<{after}&"
