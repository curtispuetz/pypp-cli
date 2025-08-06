import ast

from src.deps import Deps
from src.handle_stmt.h_class_def.util import (
    ClassMethod,
    calc_method,
    ClassField,
    calc_class_field,
)
from src.mapping.fn_arg import lookup_cpp_fn_arg


def calc_fields_and_methods_for_dataclass(
    node: ast.ClassDef,
    d: Deps,
    name_doesnt_start_with_underscore: bool,
) -> tuple[list[ClassField], list[ClassMethod]]:
    fields: list[ClassField] = []
    methods: list[ClassMethod] = []
    for item in node.body:
        if isinstance(item, ast.AnnAssign):
            fields.append(_calc_field(item, d, name_doesnt_start_with_underscore))
        elif isinstance(item, ast.FunctionDef):
            methods.append(
                calc_method(
                    item,
                    d,
                    name_doesnt_start_with_underscore,
                )
            )
        else:
            raise ValueError(
                "only field definitions and methods are supported in a dataclass"
            )
    return fields, methods


def _calc_field(
    node: ast.AnnAssign,
    d: Deps,
    name_doesnt_start_with_underscore: bool,
) -> ClassField:
    assert node.value is None, (
        "default values for dataclass attributes are not supported"
    )
    type_cpp: str = d.handle_expr(
        node.annotation,
        include_in_header=name_doesnt_start_with_underscore,
    )
    target_str: str = d.handle_expr(
        node.target, include_in_header=name_doesnt_start_with_underscore
    )
    type_str = lookup_cpp_fn_arg(type_cpp)
    return calc_class_field(type_str, target_str, target_str)
