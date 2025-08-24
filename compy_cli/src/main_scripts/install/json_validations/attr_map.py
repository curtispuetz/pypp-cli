from compy_cli.src.main_scripts.install.json_validations.util import validate_map_info


_S: str = "attr_map.json"


def validate_attr_map(attr_map: object):
    assert isinstance(attr_map, dict), f"{_S} must be a JSON object"
    for k, v in attr_map.items():
        assert isinstance(k, str), f"Key in {_S} must be a string"
        assert "." in k, f"Key {k} in {_S} must contain at least one dot"
        _validate_attr_map_entry(k, v)


def _validate_attr_map_entry(k: str, v: object):
    assert isinstance(v, dict), f"Entry for {k} in {_S} must be a JSON object"
    for kc, vc in v.items():
        assert isinstance(kc, str), f"Key in entry for {k} in {_S} must be a string"
        validate_map_info(k, kc, vc, _S)
