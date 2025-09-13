import ast

from pypp_cli.src.transpilers.other.transpiler.deps import Deps
from pypp_cli.src.transpilers.other.transpiler.module.handle_stmt.h_class_def.create_final_str import (  # noqa: E501
    create_final_str_for_class_def,
)
from pypp_cli.src.transpilers.other.transpiler.module.handle_stmt.h_class_def.for_dataclasses.calc_fields_and_methods import (  # noqa: E501
    calc_fields_and_methods_for_dataclass,
)
from pypp_cli.src.transpilers.other.transpiler.module.handle_stmt.h_class_def.for_dataclasses.calc_constructor_sig import (  # noqa: E501
    calc_constructor_signature_for_dataclass,
)


def handle_class_def_for_dataclass(
    node: ast.ClassDef,
    d: Deps,
    is_frozen: bool,
) -> str:
    is_def_in_header: bool = not d.is_main_file and not node.name.startswith("_")

    d.set_inc_in_h(is_def_in_header)
    fields, methods = calc_fields_and_methods_for_dataclass(node, d, is_def_in_header)
    constructor_sig = calc_constructor_signature_for_dataclass(fields, node.name)
    ret = create_final_str_for_class_def(
        node,
        d,
        fields,
        methods,
        constructor_sig,
        node.name.startswith("_"),
        True,
        is_frozen,
    )
    d.set_inc_in_h(False)

    return ret
