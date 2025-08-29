# Note: don't support classmethod or staticmethod. These are not necessary to have a
#  working language. So, its a thing that can be added later after a working language
#  is made (if desired).
import ast

from compy_cli.src.transpiler.module.deps import Deps
from compy_cli.src.transpiler.module.handle_stmt.h_class_def.create_final_str import (
    create_final_str_for_class_def,
)
from compy_cli.src.transpiler.module.handle_stmt.h_class_def.for_class.calc_fields_and_methods import (  # noqa: E501
    calc_methods_fields_and_base_constructor_calls_for_class,
)


def handle_class_def_for_class(node: ast.ClassDef, d: Deps) -> str:
    name_starts_with_underscore: bool = node.name.startswith("_")
    name_doesnt_start_with_underscore: bool = not name_starts_with_underscore
    d.set_inc_in_h(name_doesnt_start_with_underscore)
    fields_and_base_constructor_calls, methods, constructor_sig = (
        calc_methods_fields_and_base_constructor_calls_for_class(
            node,
            d,
            name_doesnt_start_with_underscore,
        )
    )
    ret = create_final_str_for_class_def(
        node,
        d,
        fields_and_base_constructor_calls,
        methods,
        constructor_sig,
        name_starts_with_underscore,
        is_struct=False,
    )
    d.set_inc_in_h(False)
    return ret
