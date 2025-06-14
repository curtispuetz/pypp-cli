FN_ARG_CONST_REF: set[str] = {"PyStr", "PyList", "PyDict", "PyTup", "PySet", "NpArr"}


def lookup_cpp_fn_arg(cpp_arg: str, is_const: bool) -> str:
    const_str = "const " if is_const else ""
    before_and_after = cpp_arg.split("<", 1)
    if before_and_after[0] not in FN_ARG_CONST_REF:
        return cpp_arg
    if len(before_and_after) == 1:
        return f"{const_str}{before_and_after[0]}&"
    before, after = before_and_after
    return f"{const_str}{before}<{after}&"
