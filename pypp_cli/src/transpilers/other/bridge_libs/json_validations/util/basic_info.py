from typing import Callable

from pypp_cli.src.other.library.json_validations import validate_is_list_of_strings

_N_M_AND_AN: set[str] = {"name", "module", "as_name"}


def validate_required_py_import(key_chain: list[str], v: object, S: str):
    assert isinstance(v, dict), (
        f"Entry for {'.'.join(key_chain)} in {S} must be a JSON object"
    )
    keys: set[str] = set()
    for kcc, vcc in v.items():
        assert isinstance(kcc, str), (
            f"Key in entry for {'.'.join(key_chain)} in {S} must be a string"
        )
        assert isinstance(vcc, str), (
            f"Entry for {'.'.join(key_chain + [kcc])} in {S} must be a string"
        )
        keys.add(kcc)
    assert "name" in keys, (
        f"Entry for {'.'.join(key_chain)} in {S} must include 'name' key"
    )
    keys.difference_update(_N_M_AND_AN)
    if len(keys) > 0:
        raise AssertionError(
            f"Unexpected keys {keys} in entry for {'.'.join(key_chain)} in {S}"
        )


VALIDATE_BASIC_INFO: dict[str, Callable[[list[str], object, str], None]] = {
    "quote_includes": validate_is_list_of_strings,
    "angle_includes": validate_is_list_of_strings,
    "required_py_import": validate_required_py_import,
}
