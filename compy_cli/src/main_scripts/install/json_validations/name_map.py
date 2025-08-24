from compy_cli.src.main_scripts.install.json_validations.util import validate_map_info


_S: str = "name_map.json"


def validate_name_map(name_map: object):
    assert isinstance(name_map, dict), f"{_S} must be a JSON object"
    for k, v in name_map.items():
        assert isinstance(k, str), f"Key in {_S} must be a string"
        assert isinstance(v, dict), f"Entry for {k} in {_S} must be a JSON object"
        for kc, vc in v.items():
            assert isinstance(kc, str), f"Key in entry for {k} in {_S} must be a string"
            validate_map_info(k, kc, vc, _S)
