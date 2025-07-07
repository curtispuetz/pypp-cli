import ast

from src.handle_stmt.h_class_def.create_final_str import create_final_str_for_class_def
from src.handle_stmt.h_class_def.for_dataclasses.calc_fields_and_methods import (
    calc_fields_and_methods_for_dataclass,
    calc_constructor_signature,
)
from src.util.ret_imports import RetImports


def handle_class_def_for_dataclass(
    node: ast.ClassDef,
    ret_imports: RetImports,
    ret_h_file: list[str],
    handle_stmt,
    handle_expr,
    is_frozen: bool,
) -> str:
    name_starts_with_underscore: bool = node.name.startswith("_")
    name_doesnt_start_with_underscore: bool = not name_starts_with_underscore
    fields, methods = calc_fields_and_methods_for_dataclass(
        node, ret_imports, handle_stmt, handle_expr, name_doesnt_start_with_underscore
    )
    constructor_sig = calc_constructor_signature(fields, node.name)
    return create_final_str_for_class_def(
        node,
        ret_imports,
        ret_h_file,
        handle_expr,
        fields,
        methods,
        constructor_sig,
        name_starts_with_underscore,
        name_doesnt_start_with_underscore,
        True,
        is_frozen,
    )
