from pypp_cli.src.transpilers.other.bridge_libs.json_validations.util.validate_2 import (  # noqa: E501
    validate_2,
)


_S = "always_pass_by_value.json"


def validate_always_pass_by_value(always_pass_by_value: object):
    validate_2(always_pass_by_value, _S)
