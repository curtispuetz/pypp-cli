import ast

from compy_cli.src.transpilers.other.module.deps import Deps
from compy_cli.src.transpilers.other.module.handle_stmt.h_class_def.util import (
    ClassMethod,
    calc_method,
    ClassField,
    calc_class_field,
)
from compy_cli.src.transpilers.other.module.mapping.fn_arg import lookup_cpp_fn_arg


def calc_fields_and_methods_for_dataclass(
    node: ast.ClassDef,
    d: Deps,
    name_doesnt_start_with_underscore: bool,
) -> tuple[list[ClassField | str], list[ClassMethod]]:
    fields: list[ClassField | str] = []
    methods: list[ClassMethod] = []
    for item in node.body:
        if isinstance(item, ast.AnnAssign):
            fields.append(_calc_field(item, d))
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


def _calc_field(node: ast.AnnAssign, d: Deps) -> ClassField:
    assert node.value is None, (
        "default values for dataclass attributes are not supported"
    )
    type_cpp: str = d.handle_expr(node.annotation)
    target_str: str = d.handle_expr(node.target)
    type_str = lookup_cpp_fn_arg(type_cpp, d)
    return calc_class_field(type_str, target_str, target_str)
