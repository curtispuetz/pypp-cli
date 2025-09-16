from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ClassField:
    type_cpp: str
    target_str: str
    target_other_name: str
    ref: str


def calc_class_field(type_cpp: str, name: str, other_name: str):
    if type_cpp.endswith("&"):
        ref = "&"
        type_cpp = type_cpp[:-1]
    else:
        ref = ""
    return ClassField(type_cpp, name, other_name, ref)
