def get_equals() -> str:
    # Im just testing that you can have other functiosn in the file.
    return "="


def mapping_fn(
    _type_cpp: str, target_str: str, _value_str: str, value_str_stripped: str
):
    return (
        "AnnAssignOtherType "
        + target_str
        + get_equals()
        + "AnnAssignOtherType("
        + value_str_stripped
        + ")"
    )
