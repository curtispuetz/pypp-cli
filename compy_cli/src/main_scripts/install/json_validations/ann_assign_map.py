from compy_cli.src.main_scripts.install.json_validations.util import (
    VALIDATE_BASIC_INFO,
    validate_is_list_of_strings,
)


_S = "ann_assign_map.json"


def validate_ann_assign_map(ann_assign_map: object):
    assert isinstance(ann_assign_map, dict), f"{_S} must be a JSON object"
    k = "custom_mapping_starts_with"
    assert k in ann_assign_map, f"{_S} must have a 'custom_mapping_starts_with' key"
    assert len(ann_assign_map) == 1, f"{_S} must have exactly one entry"
    for kc, vc in ann_assign_map[k].items():
        assert isinstance(kc, str), f"Key in entry for {k} in {_S} must be a string"
        assert isinstance(vc, dict), f"Entry for {k}.{kc} in {_S} must be a JSON object"
        for kcc, vcc in vc.items():
            assert isinstance(kcc, str), (
                f"Key in entry for {k}.{kc} in {_S} must be a string"
            )
            if kcc in VALIDATE_BASIC_INFO:
                VALIDATE_BASIC_INFO[kcc]([k, kc, kcc], vcc, _S)
            elif kcc == "mapping_function":
                validate_is_list_of_strings([k, kc, kcc], vcc, _S)
            else:
                raise AssertionError(
                    f"Unexpected key {kcc} in entry for {k}.{kc} in {_S}"
                )
