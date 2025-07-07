import ast

from src.d_types import AngInc
from src.handle_stmt.h_class_def.for_dataclasses.calc_fields_and_methods import (
    calc_fields_and_methods,
    DataClassMethod,
    DataClassField,
)
from src.util.calc_fn_signature import calc_fn_str_with_body
from src.util.ret_imports import RetImports, add_inc

ARG_PREFIX = "a_"


def handle_class_def_for_dataclass(
    node: ast.ClassDef,
    ret_imports: RetImports,
    ret_h_file: list[str],
    handle_stmt,
    handle_expr,
    is_frozen: bool,
) -> str:
    class_name: str = node.name
    name_starts_with_underscore: bool = class_name.startswith("_")
    name_doesnt_start_with_underscore: bool = not name_starts_with_underscore
    fields, methods = calc_fields_and_methods(
        node, ret_imports, handle_stmt, handle_expr, name_doesnt_start_with_underscore
    )
    field_defs = _calc_field_definitions(fields, is_frozen)
    c_sig: str = _calc_constructor_signature(fields, class_name)
    c_il: str = _calc_constructor_initializer_list(
        fields, ret_imports, name_doesnt_start_with_underscore
    )
    fields_and_constructor: str = f"{field_defs} {c_sig} : {c_il}" + "{}"
    if name_starts_with_underscore:
        full_methods: str = _calc_full_methods(methods)
        return _calc_final_struct(class_name, fields_and_constructor + full_methods)
    if len(methods) == 0:
        ret_h_file.append(_calc_final_struct(class_name, fields_and_constructor))
        # Nothing goes in the cpp file in this case.
        return ""
    method_signatures: str = _calc_method_signatures(methods)
    method_impls: str = _calc_method_implementations(methods, class_name)
    ret_h_file.append(
        _calc_final_struct(class_name, fields_and_constructor + method_signatures)
    )
    return method_impls


def _calc_final_struct(class_name: str, body_str: str) -> str:
    return f"struct {class_name}" + "{" + body_str + "};"


def _calc_method_signatures(methods: list[DataClassMethod]) -> str:
    ret: list[str] = []
    for method in methods:
        ret.append(method.fn_signature + ";")
    return " ".join(ret)


def _calc_full_methods(methods: list[DataClassMethod]) -> str:
    ret: list[str] = []
    for method in methods:
        ret.append(calc_fn_str_with_body(method.fn_signature, method.body_str))
    return " ".join(ret)


def _calc_method_implementations(
    methods: list[DataClassMethod], class_name: str
) -> str:
    ret: list[str] = []
    for method in methods:
        sig_with_namespace = _add_namespace(method.fn_signature, class_name)
        ret.append(calc_fn_str_with_body(sig_with_namespace, method.body_str))
    return " ".join(ret)


def _add_namespace(fn_signature: str, name: str) -> str:
    first_space = fn_signature.find(" ")
    assert first_space != -1, "shouldn't happen"
    return (
        fn_signature[: first_space + 1] + name + "::" + fn_signature[first_space + 1 :]
    )


def _calc_constructor_signature(fields: list[DataClassField], class_name: str) -> str:
    ret: list[str] = []
    for field in fields:
        ret.append(f"{field.type_cpp}{field.ref} {ARG_PREFIX}{field.target_str}")
    return class_name + "(" + ", ".join(ret) + ")"


def _calc_constructor_initializer_list(
    fields: list[DataClassField], ret_imports, name_doesnt_start_with_underscore: bool
) -> str:
    ret: list[str] = []
    for field in fields:
        if field.ref:
            ret.append(f"{field.target_str}({ARG_PREFIX}{field.target_str})")
        else:
            add_inc(
                ret_imports,
                AngInc("utility"),
                in_header=name_doesnt_start_with_underscore,
            )
            ret.append(f"{field.target_str}(std::move({ARG_PREFIX}{field.target_str}))")
    return ", ".join(ret)


def _calc_field_definitions(fields: list[DataClassField], is_frozen: bool) -> str:
    ret: list[str] = []
    const_str = "const " if is_frozen else ""
    for field in fields:
        ret.append(f"{const_str}{field.type_cpp}{field.ref} {field.target_str};")
    return " ".join(ret)
