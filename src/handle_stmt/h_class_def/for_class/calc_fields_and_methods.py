import ast

from src.handle_stmt.h_class_def.for_dataclasses.calc_fields_and_methods import (
    DataClassField,
)
from src.handle_stmt.h_class_def.util import ClassMethod, calc_method
from src.util.calc_fn_signature import calc_fn_arg_types
from src.util.ret_imports import RetImports


def calc_methods_and_fields_for_class(
    node: ast.ClassDef,
    ret_imports: RetImports,
    handle_stmt,
    handle_expr,
    name_doesnt_start_with_underscore: bool,
) -> tuple[list[DataClassField], list[ClassMethod]]:
    methods: list[ClassMethod] = []
    fields: list[DataClassField] = []
    for item in node.body:
        if isinstance(item, ast.FunctionDef):
            if item.name == "__init__":
                fields = _calc_fields(
                    item, ret_imports, handle_expr, name_doesnt_start_with_underscore
                )
                continue
            methods.append(
                calc_method(
                    item,
                    ret_imports,
                    handle_stmt,
                    handle_expr,
                    name_doesnt_start_with_underscore,
                )
            )
        else:
            raise ValueError("only methods are supported in a class definition")
    if len(fields) == 0:
        raise ValueError("class must have an __init__ method constructor")
    return fields, methods


def _calc_fields(
    node: ast.FunctionDef,
    ret_imports: RetImports,
    handle_expr,
    name_doesnt_start_with_underscore: bool,
) -> list[DataClassField]:
    ret: list[DataClassField] = []
    field_types, _ = calc_fn_arg_types(
        node,
        ret_imports,
        handle_expr,
        in_header=name_doesnt_start_with_underscore,
        skip_first_arg=True,
    )
    assert len(field_types) > 0, "at least one field is required in __init__"
    field_names = _calc_field_names(
        node, ret_imports, handle_expr, name_doesnt_start_with_underscore
    )
    for t, n in zip(field_types, field_names):
        if t.endswith("&"):
            ref = "&"
            type_cpp = t[:-1]
        else:
            ref = ""
            type_cpp = t
        ret.append(DataClassField(type_cpp=type_cpp, target_str=n, ref=ref))
    return ret


def _calc_field_names(
    node: ast.FunctionDef,
    ret_imports: RetImports,
    handle_expr,
    name_doesnt_start_with_underscore: bool,
) -> list[str]:
    ret: list[str] = []
    for item in node.body:
        if isinstance(item, ast.Assign):
            assert len(item.targets) == 1, (
                "only one target is supported for field names in __init__"
            )
            ret.append(
                handle_expr(
                    item.targets[0],
                    ret_imports,
                    include_in_header=name_doesnt_start_with_underscore,
                )
            )
        else:
            raise ValueError(
                "only field assignments without type annotation are supported in __init__"
            )
    return ret
