from .util.validate_1 import BASE_VALIDATE_ENTRY_MAP, validate_1


_S: str = "name_map.json"


def validate_name_map(name_map: object):
    validate_1(name_map, BASE_VALIDATE_ENTRY_MAP, _S)
