from compy_cli.src.package_manager.installer.json_validations.util.validate_2 import (
    validate_2,
)


_S = "subscriptable_types.json"


def validate_subscriptable_types(subscriptable_types: object):
    validate_2(subscriptable_types, _S)
