from compy_cli.src.transpilers.other.bridge_libs.json_validations.util.validate_2 import (  # noqa: E501
    validate_2,
)


_S = "subscriptable_types.json"


def validate_subscriptable_types(subscriptable_types: object):
    validate_2(subscriptable_types, _S)
