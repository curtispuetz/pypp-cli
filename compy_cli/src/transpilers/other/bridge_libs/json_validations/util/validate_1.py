from typing import Callable
from compy_cli.src.transpilers.other.bridge_libs.json_validations.util.basic_info import (  # noqa: E501
    VALIDATE_BASIC_INFO,
)
from compy_cli.src.transpilers.other.module.mapping.util import calc_funcs_in_str
from compy_cli.src.other.library.json_validations import (
    validate_is_list_of_strings,
)


def _validate_is_single_mapping_fn(key_chain: list[str], v: object, S: str):
    validate_is_list_of_strings(key_chain, v, S)
    assert isinstance(v, list), "shouldn't happen"
    funcs = calc_funcs_in_str("\n".join(v))
    assert len(funcs) == 1, (
        f"Expected exactly one function in mapping_function in {S}. Instead got "
        f"list: {[f.__name__ for f in funcs]}"
    )


def validate_to_string(key_chain: list[str], vc: dict, S: str):
    for kcc, vcc in vc.items():
        assert isinstance(kcc, str), (
            f"Key in entry for {'.'.join(key_chain)} in {S} must be a string"
        )
        if kcc in VALIDATE_BASIC_INFO:
            VALIDATE_BASIC_INFO[kcc](key_chain + [kcc], vcc, S)
        elif kcc == "to":
            assert isinstance(vcc, str), (
                f"Entry for {'.'.join(key_chain + [kcc])} in {S} must be a string"
            )
        else:
            raise AssertionError(
                f"Unexpected key {kcc} in entry for {'.'.join(key_chain)} in {S}"
            )


def validate_custom_mapping(key_chain: list[str], vc: dict, S: str):
    for kcc, vcc in vc.items():
        assert isinstance(kcc, str), (
            f"Key in entry for {'.'.join(key_chain)} in {S} must be a string"
        )
        if kcc in VALIDATE_BASIC_INFO:
            VALIDATE_BASIC_INFO[kcc](key_chain + [kcc], vcc, S)
        elif kcc == "mapping_function":
            _validate_is_single_mapping_fn(key_chain + [kcc], vcc, S)
        else:
            raise AssertionError(
                f"Unexpected key {kcc} in entry for {'.'.join(key_chain)} in {S}"
            )


def validate_replace_dot_with_double_colon(key_chain: list[str], vc: dict, S: str):
    for kcc, vcc in vc.items():
        assert isinstance(kcc, str), (
            f"Key in entry for {'.'.join(key_chain)} in {S} must be a string"
        )
        if kcc in VALIDATE_BASIC_INFO:
            VALIDATE_BASIC_INFO[kcc](key_chain + [kcc], vcc, S)
        else:
            raise AssertionError(
                f"Unexpected key {kcc} in entry for {'.'.join(key_chain)} in {S}"
            )


BASE_VALIDATE_ENTRY_MAP: dict[str, Callable[[list[str], dict, str], None]] = {
    "to_string": validate_to_string,
    "custom_mapping": validate_custom_mapping,
    "custom_mapping_starts_with": validate_custom_mapping,
}


def validate_1(map: object, validate_entry_map, S: str):
    assert isinstance(map, dict), f"{S} must be a JSON object"
    for k, v in map.items():
        assert isinstance(k, str), f"Key in {S} must be a string"
        assert k in validate_entry_map, f"Unexpected key {k} in {S}"
        assert isinstance(v, dict), f"Entry for {k} in {S} must be a JSON object"
        for kc, vc in v.items():
            assert isinstance(kc, str), f"Key in entry for {k} in {S} must be a string"
            assert isinstance(vc, dict), (
                f"Entry for {k}.{kc} in {S} must be a JSON object"
            )
            validate_entry_map[k]([k, kc], vc, S)
