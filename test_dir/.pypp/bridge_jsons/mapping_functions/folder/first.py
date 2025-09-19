def mapping_function(
    _type_cpp: str, target_str: str, _value_str: str, value_str_stripped: str
):
    return (
        "AnnAssignOtherType "
        + target_str
        + "="
        + "AnnAssignOtherType("
        + value_str_stripped
        + ")"
    )
