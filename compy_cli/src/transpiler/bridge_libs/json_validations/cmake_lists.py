from compy_cli.src.transpiler.bridge_libs.json_validations.util.validations import (
    validate_is_list_of_strings,
)


_S: str = "cmake_lists.json"
_AL_AND_LL: set[str] = {"add_lines", "link_libraries"}


def validate_cmake_lists(cmake_lists: object):
    assert isinstance(cmake_lists, dict), f"{_S} must be a JSON object"
    for k, v in cmake_lists.items():
        assert isinstance(k, str), f"Key in {_S} must be a string"
        if k in _AL_AND_LL:
            validate_is_list_of_strings([k], v, _S)
        else:
            raise AssertionError(f"Unexpected key '{k}' in {_S}")
