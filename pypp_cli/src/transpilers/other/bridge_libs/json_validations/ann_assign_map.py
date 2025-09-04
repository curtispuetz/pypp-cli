from pypp_cli.src.transpilers.other.bridge_libs.json_validations.util.validate_1 import (  # noqa: E501
    BASE_VALIDATE_ENTRY_MAP,
    validate_1,
)


_S = "ann_assign_map.json"


def validate_ann_assign_map(ann_assign_map: object):
    validate_1(ann_assign_map, BASE_VALIDATE_ENTRY_MAP, _S)
