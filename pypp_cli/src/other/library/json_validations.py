def validate_is_list_of_strings(key_chain: list[str], v: object, json_file_name: str):
    assert isinstance(v, list), (
        f"Entry for {'.'.join(key_chain)} in {json_file_name} must be a list"
    )
    for item in v:
        assert isinstance(item, str), (
            f"Item in entry for {'.'.join(key_chain)} in {json_file_name} "
            f"must be a string"
        )


def validate_is_dict_of_strings(key_chain: list[str], v: object, json_file_name: str):
    assert isinstance(v, dict), (
        f"Entry for {'.'.join(key_chain)} in {json_file_name} must be a JSON object"
    )
    for k, val in v.items():
        assert isinstance(k, str), (
            f"Key in entry for {'.'.join(key_chain)} in {json_file_name} must be a "
            f"string"
        )
        assert isinstance(val, str), (
            f"Entry for {'.'.join(key_chain + [k])} in {json_file_name} must be a "
            f"string"
        )
