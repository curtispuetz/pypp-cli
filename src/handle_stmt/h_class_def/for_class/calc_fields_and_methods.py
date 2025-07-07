import ast

from src.handle_stmt.h_class_def.util import (
    ClassMethod,
    calc_method,
    ClassField,
    calc_class_field, ARG_PREFIX,
)
from src.util.calc_fn_signature import calc_fn_arg_types
from src.util.handle_lists import handle_exprs
from src.util.ret_imports import RetImports


def calc_methods_fields_and_base_constructor_calls_for_class(
    node: ast.ClassDef,
    ret_imports: RetImports,
    handle_stmt,
    handle_expr,
    name_doesnt_start_with_underscore: bool,
) -> tuple[list[ClassField], list[ClassMethod | str], str]:
    methods: list[ClassMethod] = []
    fields_and_base_constructor_calls: list[ClassField] = []
    constructor_sig = ""
    for item in node.body:
        if isinstance(item, ast.FunctionDef):
            if item.name == "__init__":
                field_types = calc_fn_arg_types(
                    item,
                    ret_imports,
                    handle_expr,
                    in_header=name_doesnt_start_with_underscore,
                    skip_first_arg=True,
                )
                fields_and_base_constructor_calls = (
                    _calc_fields_and_base_constructor_calls(
                        item,
                        ret_imports,
                        field_types,
                        handle_expr,
                        name_doesnt_start_with_underscore,
                    )
                )
                constructor_sig = _calc_constructor_signature(node.name, field_types)
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
    if len(fields_and_base_constructor_calls) == 0:
        raise ValueError("class must have an __init__ method constructor")
    return fields_and_base_constructor_calls, methods, constructor_sig


# TODO: move to a different file
def _calc_constructor_signature(class_name: str, field_types: dict[str, str]) -> str:
    ret: list[str] = []
    for n, t in field_types.items():
        ret.append(f"{t} {ARG_PREFIX}{n}")
    return class_name + "(" + ", ".join(ret) + ")"


def _calc_fields_and_base_constructor_calls(
    node: ast.FunctionDef,
    ret_imports: RetImports,
    field_types: dict[str, str],
    handle_expr,
    name_doesnt_start_with_underscore: bool,
) -> list[ClassField | str]:
    ret: list[ClassField | str] = []
    assert len(field_types) > 0, "at least one field is required in __init__"
    for item in node.body:
        if isinstance(item, ast.Assign):
            assert len(item.targets) == 1, (
                "only one target is supported for field names in __init__"
            )
            field_name = handle_expr(
                item.targets[0],
                ret_imports,
                include_in_header=name_doesnt_start_with_underscore,
            )
            assign_name = handle_expr(
                item.value,
                ret_imports,
                include_in_header=name_doesnt_start_with_underscore,
            )
            ret.append(calc_class_field(field_types[assign_name], field_name))
        elif isinstance(item, ast.Expr):
            assert isinstance(item.value, ast.Call), (
                "only field assignments without type annotation are supported in __init__"
            )
            assert isinstance(item.value.func, ast.Attribute), (
                "only field assignments without type annotation are supported in __init__"
            )
            assert item.value.func.attr == "__init__", (
                "only field assignments without type annotation are supported in __init__"
            )
            args_str_list: list[str] = []
            for arg in item.value.args[1:]:
                args_str_list.append(
                    ARG_PREFIX + handle_expr(
                        arg,
                        ret_imports,
                        include_in_header=name_doesnt_start_with_underscore,
                    )
                )
            args_str = ", ".join(args_str_list)
            base_class_name = handle_expr(
                item.value.func.value,
                ret_imports,
                include_in_header=name_doesnt_start_with_underscore,
            )
            ret.append(f"{base_class_name}({args_str})")
        else:
            raise ValueError(
                "only field assignments without type annotation are supported in __init__"
            )
    return ret
