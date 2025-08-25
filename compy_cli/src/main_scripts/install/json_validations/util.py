from typing import Callable


_Q_AND_A: set[str] = {"quote_include", "angle_include"}
_N_M_AND_AN: set[str] = {"name", "module", "as_name"}


def _validate_cpp_type(key_chain: list[str], v: object, S: str):
    assert isinstance(v, str), (
        f"Entry for {'.'.join(key_chain)} in {S} must be a string"
    )


def _validate_cpp_includes(key_chain: list[str], v: object, S: str):
    assert isinstance(v, dict), (
        f"Entry for {'.'.join(key_chain)} in {S} must be a JSON object"
    )
    for kcc, vcc in v.items():
        assert isinstance(kcc, str), (
            f"Key in entry for {'.'.join(key_chain)} in {S} must be a string"
        )
        if kcc not in _Q_AND_A:
            raise AssertionError(
                f"Unexpected key {kcc} in entry for {'.'.join(key_chain)} in {S}"
            )
        assert isinstance(vcc, str), (
            f"Entry for {'.'.join(key_chain + [kcc])} in {S} must be a string"
        )


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
    "cpp_includes": _validate_cpp_includes,
    "required_py_import": validate_required_py_import,
}


def validate_map_info(k: str, kc: str, vc: object, S: str):
    if kc in VALIDATE_BASIC_INFO:
        VALIDATE_BASIC_INFO[kc]([k, kc], vc, S)
    elif kc == "cpp_type":
        _validate_cpp_type([k, kc], vc, S)
    else:
        raise AssertionError(f"Unexpected key {kc} in entry for {k} in {S}")


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
