from pypp_cli.src.transpilers.other.transpiler.module.handle_stmt.h_class_def.util import (  # noqa: E501
    ClassField,
    ARG_PREFIX,
)


def calc_constructor_signature_for_dataclass(
    fields: list[ClassField | str], class_name: str
) -> str:
    ret: list[str] = []
    for field in fields:
        assert isinstance(field, ClassField), "shouldn't happen"
        ret.append(f"{field.type_cpp}{field.ref} {ARG_PREFIX}{field.target_str}")
    return class_name + "(" + ", ".join(ret) + ")"
