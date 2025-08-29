import ast

from compy_cli.src.transpiler.deps import Deps
from compy_cli.src.transpiler.handle_stmt.h_class_def.for_class.calc_constructor_sig import (
    calc_constructor_signature_for_class,
)
from compy_cli.src.transpiler.handle_stmt.h_class_def.util import (
    ClassMethod,
    calc_method,
    ClassField,
    calc_class_field,
    ARG_PREFIX,
)
from compy_cli.src.transpiler.util.calc_fn_signature import calc_fn_arg_types


def calc_methods_fields_and_base_constructor_calls_for_class(
    node: ast.ClassDef,
    d: Deps,
    name_doesnt_start_with_underscore: bool,
) -> tuple[list[ClassField | str], list[ClassMethod], str]:
    methods: list[ClassMethod] = []
    fields_and_base_constructor_calls: list[ClassField | str] = []
    constructor_sig = ""
    for item in node.body:
        if isinstance(item, ast.FunctionDef):
            if item.name == "__init__":
                field_types = calc_fn_arg_types(
                    item,
                    d,
                    skip_first_arg=True,
                )
                fields_and_base_constructor_calls = (
                    _calc_fields_and_base_constructor_calls(item, d, field_types)
                )
                constructor_sig = calc_constructor_signature_for_class(
                    node.name, field_types
                )
                continue
            methods.append(
                calc_method(
                    item,
                    d,
                    name_doesnt_start_with_underscore,
                )
            )
        else:
            raise ValueError("only methods are supported in a class definition")
    return fields_and_base_constructor_calls, methods, constructor_sig


def _calc_fields_and_base_constructor_calls(
    node: ast.FunctionDef, d: Deps, field_types: dict[str, str]
) -> list[ClassField | str]:
    ret: list[ClassField | str] = []
    assert len(field_types) > 0, "at least one field is required in __init__"
    for item in node.body:
        if isinstance(item, ast.Assign):
            assert len(item.targets) == 1, (
                "only one target is supported for field names in __init__"
            )
            field_name = d.handle_expr(item.targets[0])
            assign_name = d.handle_expr(item.value)
            ret.append(
                calc_class_field(field_types[assign_name], field_name, assign_name)
            )
        elif isinstance(item, ast.Expr):
            error_str: str = (
                "only field assignments without type annotation are "
                "supported in __init__"
            )
            assert isinstance(item.value, ast.Call), error_str
            assert isinstance(item.value.func, ast.Attribute), error_str
            assert item.value.func.attr == "__init__", error_str
            args_str_list: list[str] = []
            for arg in item.value.args[1:]:
                args_str_list.append(ARG_PREFIX + d.handle_expr(arg))
            args_str = ", ".join(args_str_list)
            base_class_name = d.handle_expr(item.value.func.value)
            ret.append(f"{base_class_name}({args_str})")
        else:
            raise ValueError(error_str)
    return ret
