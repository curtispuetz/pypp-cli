from compy_cli.src.transpiler.bridge_libs.json_validations.util.validate_2 import (
    validate_2,
)


_S = "always_pass_by_value.json"


def validate_always_pass_by_value(always_pass_by_value: object):
    validate_2(always_pass_by_value, _S)
