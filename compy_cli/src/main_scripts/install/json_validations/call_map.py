from typing import Callable


from compy_cli.src.main_scripts.install.json_validations.util.basic_info import (
    VALIDATE_BASIC_INFO,
)
from compy_cli.src.main_scripts.install.json_validations.util.validate_1 import (
    BASE_VALIDATE_ENTRY_MAP,
    validate_1,
    validate_replace_dot_with_double_colon,
)


_S: str = "call_map.json"
_L_OR_R = {"left", "right"}


def _validate_left_and_right(key_chain: list[str], vc: dict, S: str):
    for kcc, vcc in vc.items():
        assert isinstance(kcc, str), (
            f"Key in entry for {'.'.join(key_chain)} in {S} must be a string"
        )
        if kcc in VALIDATE_BASIC_INFO:
            VALIDATE_BASIC_INFO[kcc](key_chain + [kcc], vcc, S)
        elif kcc in _L_OR_R:
            assert isinstance(vcc, str), (
                f"Entry for {'.'.join(key_chain + [kcc])} in {S} must be a string"
            )
        else:
            raise AssertionError(
                f"Unexpected key {kcc} in entry for {'.'.join(key_chain)} in {S}"
            )


VALIDATE_CALL_ENTRY_MAP: dict[str, Callable[[list[str], dict, str], None]] = {
    **BASE_VALIDATE_ENTRY_MAP,
    "left_and_right": _validate_left_and_right,
    "replace_dot_with_double_colon": validate_replace_dot_with_double_colon,
}


def validate_call_map(call_map: object):
    validate_1(call_map, VALIDATE_CALL_ENTRY_MAP, _S)
