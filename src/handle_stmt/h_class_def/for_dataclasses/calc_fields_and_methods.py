import ast

from src.handle_stmt.h_class_def.util import (
    ClassMethod,
    calc_method,
    ClassField,
    calc_class_field,
)
from src.mapping.fn_arg import lookup_cpp_fn_arg
from src.util.ret_imports import RetImports


def calc_fields_and_methods_for_dataclass(
    node: ast.ClassDef,
    ret_imports: RetImports,
    handle_stmt,
    handle_expr,
    name_doesnt_start_with_underscore: bool,
) -> tuple[list[ClassField], list[ClassMethod]]:
    fields: list[ClassField] = []
    methods: list[ClassMethod] = []
    for item in node.body:
        if isinstance(item, ast.AnnAssign):
            fields.append(
                _calc_field(
                    item, ret_imports, handle_expr, name_doesnt_start_with_underscore
                )
            )
        elif isinstance(item, ast.FunctionDef):
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
            raise ValueError(
                "only field definitions and methods are supported in a dataclass"
            )
    return fields, methods


def _calc_field(
    node: ast.AnnAssign,
    ret_imports: RetImports,
    handle_expr,
    name_doesnt_start_with_underscore: bool,
) -> ClassField:
    assert node.value is None, (
        "default values for dataclass attributes are not supported"
    )
    type_cpp: str = handle_expr(
        node.annotation,
        ret_imports,
        include_in_header=name_doesnt_start_with_underscore,
    )
    target_str: str = handle_expr(
        node.target, ret_imports, include_in_header=name_doesnt_start_with_underscore
    )
    type_str = lookup_cpp_fn_arg(type_cpp)
    return calc_class_field(type_str, target_str)
