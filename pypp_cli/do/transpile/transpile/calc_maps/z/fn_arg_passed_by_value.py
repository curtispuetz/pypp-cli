def fn_arg_passed_by_value_warning_msg(lib: str, full_type_str: str) -> str:
    return (
        f"Py++ transpiler already passes the type {full_type_str} by value always. "
        f"Library {lib} is potentially changing this behavior."
    )
