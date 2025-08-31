import ast

from compy_cli.src.transpilers.other.module.deps import Deps
from compy_cli.src.transpilers.other.module.handle_stmt.h_class_def.create_final_str import (  # noqa: E501
    create_final_str_for_class_def,
)
from compy_cli.src.transpilers.other.module.handle_stmt.h_class_def.for_dataclasses.calc_fields_and_methods import (  # noqa: E501
    calc_fields_and_methods_for_dataclass,
)
from compy_cli.src.transpilers.other.module.handle_stmt.h_class_def.for_dataclasses.calc_constructor_sig import (  # noqa: E501
    calc_constructor_signature_for_dataclass,
)


def handle_class_def_for_dataclass(
    node: ast.ClassDef,
    d: Deps,
    is_frozen: bool,
) -> str:
    name_starts_with_underscore: bool = node.name.startswith("_")
    name_doesnt_start_with_underscore: bool = not name_starts_with_underscore
    d.set_inc_in_h(name_doesnt_start_with_underscore)
    fields, methods = calc_fields_and_methods_for_dataclass(
        node, d, name_doesnt_start_with_underscore
    )
    constructor_sig = calc_constructor_signature_for_dataclass(fields, node.name)
    ret = create_final_str_for_class_def(
        node,
        d,
        fields,
        methods,
        constructor_sig,
        name_starts_with_underscore,
        True,
        is_frozen,
    )
    d.set_inc_in_h(False)
    return ret
