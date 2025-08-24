from compy_cli.src.main_scripts.install.json_validations.subscriptable_types import (
    validate_helper,
)


_S = "always_pass_by_value.json"


def validate_always_pass_by_value(always_pass_by_value: object):
    validate_helper(always_pass_by_value, _S)
