from compy_cli.src.package_manager.installer.json_validations.util.validations import (
    validate_is_list_of_strings,
)


_S = "import_map.json"
_D = "direct_to_cpp_include"
_I = "ignore"


def validate_import_map(import_map: object):
    assert isinstance(import_map, dict), f"{_S} must be a JSON object"
    assert len(import_map) == 1, (
        f"{_S} must have exactly one entry (either 'direct_to_cpp_include' or 'ignore')"
    )
    if _D in import_map:
        validate_is_list_of_strings([_D], import_map[_D], _S)
    elif _I in import_map:
        validate_is_list_of_strings([_I], import_map[_I], _S)
    else:
        raise AssertionError(f"Unexpected key {list(import_map.keys())[0]} in {_S}")
