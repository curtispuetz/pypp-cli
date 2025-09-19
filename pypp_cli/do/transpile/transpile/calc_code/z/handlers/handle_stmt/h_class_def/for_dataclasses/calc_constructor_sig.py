from .class_field_calculator import ClassField
from .constants import ARG_PREFIX


def calc_constructor_signature_for_dataclass(
    fields: list[ClassField], class_name: str
) -> str:
    ret: list[str] = []
    for field in fields:
        ret.append(f"{field.type_cpp}{field.ref} {ARG_PREFIX}{field.target_str}")
    return class_name + "(" + ", ".join(ret) + ")"
