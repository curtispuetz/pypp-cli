import ast

from src.d_types import AngInc
from src.deps import Deps
from src.handle_stmt.h_class_def.util import ClassMethod, ClassField, ARG_PREFIX
from src.util.calc_fn_signature import calc_fn_str_with_body
from src.util.ret_imports import RetImports, add_inc


def create_final_str_for_class_def(
    node: ast.ClassDef,
    d: Deps,
    fields_and_base_constructor_calls: list[ClassField | str],
    methods: list[ClassMethod],
    constructor_sig: str,
    name_starts_with_underscore: bool,
    name_doesnt_start_with_underscore: bool,
    is_struct: bool,
    is_frozen: bool = False,
):
    class_name: str = node.name
    fields_and_constructor: str = _calc_fields_and_constructor(
        fields_and_base_constructor_calls,
        constructor_sig,
        d.ret_imports,
        name_doesnt_start_with_underscore,
        is_frozen,
    )
    base_classes: list[str] = _calc_base_classes(
        node, d, name_doesnt_start_with_underscore
    )
    if name_starts_with_underscore:
        full_methods: str = _calc_full_methods(methods)
        return _calc_final_str(
            class_name, fields_and_constructor + full_methods, is_struct, base_classes
        )
    if len(methods) == 0:
        d.ret_h_file.append(
            _calc_final_str(class_name, fields_and_constructor, is_struct, base_classes)
        )
        # Nothing goes in the cpp file in this case.
        return ""
    method_signatures: str = _calc_method_signatures(methods)
    method_impls: str = _calc_method_implementations(methods, class_name)
    d.ret_h_file.append(
        _calc_final_str(
            class_name,
            fields_and_constructor + method_signatures,
            is_struct,
            base_classes,
        )
    )
    return method_impls


def _calc_final_str(
    class_name: str, body_str: str, is_struct: bool, base_classes: list[str]
) -> str:
    bc: list[str] = []
    for base in base_classes:
        bc.append(f"public {base}")
    base_classes_str = ", ".join(bc)
    if base_classes_str != "":
        base_classes_str = ": " + base_classes_str
    if is_struct:
        s = "struct"
        public = ""
    else:
        s = "class"
        public = "public:"
    return f"{s} {class_name} {base_classes_str}" + "{" + public + body_str + "};\n\n"


def _calc_base_classes(
    node: ast.ClassDef,
    d: Deps,
    name_doesnt_start_with_underscore: bool,
) -> list[str]:
    ret: list[str] = []
    for base in node.bases:
        ret.append(
            d.handle_expr(base, include_in_header=name_doesnt_start_with_underscore)
        )
    return ret


def _calc_fields_and_constructor(
    fields_and_base_constructor_calls: list[ClassField | str],
    constructor_sig: str,
    ret_imports: RetImports,
    name_doesnt_start_with_underscore: bool,
    is_frozen: bool,
):
    if constructor_sig == "":
        # There can't be any fields if there is no constructor.
        return ""
    field_defs = _calc_field_definitions(fields_and_base_constructor_calls, is_frozen)
    c_il: str = _calc_constructor_initializer_list(
        fields_and_base_constructor_calls,
        ret_imports,
        name_doesnt_start_with_underscore,
    )
    return f"{field_defs} {constructor_sig} : {c_il}" + "{}"


def _calc_method_signatures(methods: list[ClassMethod]) -> str:
    ret: list[str] = []
    for method in methods:
        ret.append(method.fn_signature + ";")
    return " ".join(ret)


def _calc_full_methods(methods: list[ClassMethod]) -> str:
    ret: list[str] = []
    for method in methods:
        ret.append(calc_fn_str_with_body(method.fn_signature, method.body_str))
    return "\n\n".join(ret)


def _calc_method_implementations(methods: list[ClassMethod], class_name: str) -> str:
    ret: list[str] = []
    for method in methods:
        sig_with_namespace = _add_namespace(method.fn_signature, class_name)
        ret.append(calc_fn_str_with_body(sig_with_namespace, method.body_str))
    return "\n\n".join(ret)


def _add_namespace(fn_signature: str, name: str) -> str:
    first_space = fn_signature.find(" ")
    assert first_space != -1, "shouldn't happen"
    return (
        fn_signature[: first_space + 1] + name + "::" + fn_signature[first_space + 1 :]
    )


def _calc_constructor_initializer_list(
    fields_and_base_constructor_calls: list[ClassField | str],
    ret_imports,
    name_doesnt_start_with_underscore: bool,
) -> str:
    ret: list[str] = []
    for field in fields_and_base_constructor_calls:
        if isinstance(field, str):
            ret.append(field)
            continue
        if field.ref:
            ret.append(f"{field.target_str}({ARG_PREFIX}{field.target_other_name})")
        else:
            add_inc(
                ret_imports,
                AngInc("utility"),
                in_header=name_doesnt_start_with_underscore,
            )
            ret.append(
                f"{field.target_str}(std::move({ARG_PREFIX}{field.target_other_name}))"
            )
    return ", ".join(ret)


def _calc_field_definitions(fields: list[ClassField | str], is_frozen: bool) -> str:
    ret: list[str] = []
    const_str = "const " if is_frozen else ""
    for field in fields:
        if isinstance(field, str):
            continue
        ret.append(f"{const_str}{field.type_cpp}{field.ref} {field.target_str};")
    return " ".join(ret)
