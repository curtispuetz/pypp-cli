from collections.abc import Callable


from compy_cli.src.main_scripts.install.json_validations.util import (
    VALIDATE_BASIC_INFO,
    validate_is_list_of_strings,
)


_S: str = "call_map.json"
_L_OR_R = {"left", "right"}


def _validate_left_and_right(key_chain: list[str], vc: dict):
    for kcc, vcc in vc.items():
        assert isinstance(kcc, str), (
            f"Key in entry for {'.'.join(key_chain)} in {_S} must be a string"
        )
        if kcc in VALIDATE_BASIC_INFO:
            VALIDATE_BASIC_INFO[kcc](key_chain + [kcc], vcc, _S)
        elif kcc in _L_OR_R:
            assert isinstance(vcc, str), (
                f"Entry for {'.'.join(key_chain + [kcc])} in {_S} must be a string"
            )
        else:
            raise AssertionError(
                f"Unexpected key {kcc} in entry for {'.'.join(key_chain)} in {_S}"
            )


def _validate_to_string(key_chain: list[str], vc: dict):
    for kcc, vcc in vc.items():
        assert isinstance(kcc, str), (
            f"Key in entry for {'.'.join(key_chain)} in {_S} must be a string"
        )
        if kcc in VALIDATE_BASIC_INFO:
            VALIDATE_BASIC_INFO[kcc](key_chain + [kcc], vcc, _S)
        elif kcc == "to":
            assert isinstance(vcc, str), (
                f"Entry for {'.'.join(key_chain + [kcc])} in {_S} must be a string"
            )
        else:
            raise AssertionError(
                f"Unexpected key {kcc} in entry for {'.'.join(key_chain)} in {_S}"
            )


def _validate_custom_mapping(key_chain: list[str], vc: dict):
    for kcc, vcc in vc.items():
        assert isinstance(kcc, str), (
            f"Key in entry for {'.'.join(key_chain)} in {_S} must be a string"
        )
        if kcc in VALIDATE_BASIC_INFO:
            VALIDATE_BASIC_INFO[kcc](key_chain + [kcc], vcc, _S)
        elif kcc == "mapping_function":
            validate_is_list_of_strings(key_chain + [kcc], vcc, _S)
        else:
            raise AssertionError(
                f"Unexpected key {kcc} in entry for {'.'.join(key_chain)} in {_S}"
            )


def _validate_replace_dot_with_double_colon(key_chain: list[str], vc: dict):
    for kcc, vcc in vc.items():
        assert isinstance(kcc, str), (
            f"Key in entry for {'.'.join(key_chain)} in {_S} must be a string"
        )
        if kcc in VALIDATE_BASIC_INFO:
            VALIDATE_BASIC_INFO[kcc](key_chain + [kcc], vcc, _S)
        else:
            raise AssertionError(
                f"Unexpected key {kcc} in entry for {'.'.join(key_chain)} in {_S}"
            )


VALIDATE_CALL_ENTRY: dict[str, Callable[[list[str], dict], None]] = {
    "left_and_right": _validate_left_and_right,
    "to_string": _validate_to_string,
    "custom_mapping": _validate_custom_mapping,
    "custom_mapping_starts_with": _validate_custom_mapping,
    "replace_dot_with_double_colon": _validate_replace_dot_with_double_colon,
}


def validate_call_map(call_map: object):
    assert isinstance(call_map, dict), f"{_S} must be a JSON object"
    for k, v in call_map.items():
        assert isinstance(k, str), f"Key in {_S} must be a string"
        assert k in VALIDATE_CALL_ENTRY, f"Unexpected key {k} in {_S}"
        assert isinstance(v, dict), f"Entry for {k} in {_S} must be a JSON object"
        for kc, vc in v.items():
            assert isinstance(kc, str), f"Key in entry for {k} in {_S} must be a string"
            assert isinstance(vc, dict), (
                f"Entry for {k}.{kc} in {_S} must be a JSON object"
            )
            VALIDATE_CALL_ENTRY[k]([k, kc], vc)
