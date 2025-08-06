import ast

from src.deps import Deps
from src.handle_stmt.h_class_def.create_final_str import create_final_str_for_class_def
from src.handle_stmt.h_class_def.for_dataclasses.calc_fields_and_methods import (
    calc_fields_and_methods_for_dataclass,
)
from src.handle_stmt.h_class_def.for_dataclasses.calc_constructor_sig import (
    calc_constructor_signature_for_dataclass,
)


def handle_class_def_for_dataclass(
    node: ast.ClassDef,
    d: Deps,
    is_frozen: bool,
) -> str:
    name_starts_with_underscore: bool = node.name.startswith("_")
    name_doesnt_start_with_underscore: bool = not name_starts_with_underscore
    fields, methods = calc_fields_and_methods_for_dataclass(
        node, d, name_doesnt_start_with_underscore
    )
    constructor_sig = calc_constructor_signature_for_dataclass(fields, node.name)
    return create_final_str_for_class_def(
        node,
        d,
        fields,
        methods,
        constructor_sig,
        name_starts_with_underscore,
        name_doesnt_start_with_underscore,
        True,
        is_frozen,
    )
