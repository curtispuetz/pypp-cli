from pypp_cli.y.constants import TRANSPILER_CONFIG_DIR


def fn_arg_passed_by_value_warning_msg(lib: str, full_type_str: str):
    print(
        f"WARNING: Py++ transpiler already passes the type {full_type_str} by value "
        f"always. "
        f"Library {lib} is potentially changing this behavior."
    )


def fn_arg_passed_by_value_warning_msg_local(full_type_str: str):
    print(
        f"WARNING: Py++ transpiler already passes the type {full_type_str} by value "
        f"always. "
        f".pypp/{TRANSPILER_CONFIG_DIR}/always_pass_by_value.json is potentially "
        f"changing this "
        f"behavior."
    )
