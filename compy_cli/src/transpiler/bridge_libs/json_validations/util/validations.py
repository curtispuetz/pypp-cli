def validate_is_list_of_strings(key_chain: list[str], v: object, S: str):
    assert isinstance(v, list), f"Entry for {'.'.join(key_chain)} in {S} must be a list"
    for item in v:
        assert isinstance(item, str), (
            f"Item in entry for {'.'.join(key_chain)} in {S} must be a string"
        )


def validate_is_dict_of_strings(key_chain: list[str], v: object, S: str):
    assert isinstance(v, dict), (
        f"Entry for {'.'.join(key_chain)} in {S} must be a JSON object"
    )
    for k, val in v.items():
        assert isinstance(k, str), (
            f"Key in entry for {'.'.join(key_chain)} in {S} must be a string"
        )
        assert isinstance(val, str), (
            f"Entry for {'.'.join(key_chain + [k])} in {S} must be a string"
        )
