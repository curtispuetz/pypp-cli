# Note: don't support classmethod or staticmethod. These are not necessary to have a
#  working language. So, its a thing that can be added later after a working language
#  is made (if desired).
import ast

from src.handle_stmt.h_class_def.create_final_str import create_final_str_for_class_def
from src.handle_stmt.h_class_def.for_class.calc_fields_and_methods import (
    calc_methods_and_fields_for_class,
)
from src.util.ret_imports import RetImports


def handle_class_def_for_class(
    node: ast.ClassDef,
    ret_imports: RetImports,
    ret_h_file: list[str],
    handle_stmt,
    handle_expr,
) -> str:
    class_name: str = node.name
    name_starts_with_underscore: bool = class_name.startswith("_")
    name_doesnt_start_with_underscore: bool = not name_starts_with_underscore
    fields, methods = calc_methods_and_fields_for_class(
        node, ret_imports, handle_stmt, handle_expr, name_doesnt_start_with_underscore
    )
    return create_final_str_for_class_def(
        ret_imports,
        ret_h_file,
        fields,
        methods,
        class_name,
        name_starts_with_underscore,
        name_doesnt_start_with_underscore,
        is_struct=False,
    )
