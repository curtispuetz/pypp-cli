import ast
from dataclasses import dataclass

from pypp_cli.do.z_i.config import SHOULDNT_HAPPEN
from pypp_cli.do.transpile.transpile.z_i.d_types import AngInc
from pypp_cli.do.transpile.transpile.handle.node import Deps
from .class_field_calculator import ClassField
from .method_calculator import ClassMethod
from .constants import ARG_PREFIX
from pypp_cli.do.transpile.transpile.handle.z.handlers.util.calc_fn_signature import (
    calc_fn_str_with_body,
)


@dataclass(frozen=True, slots=True)
class DataclassFinalStrCreator:
    _d: Deps

    def create(
        self,
        node: ast.ClassDef,
        fields_and_base_constructor_calls: list[ClassField],
        methods: list[ClassMethod],
        constructor_sig: str,
        name_starts_with_underscore: bool,
        is_struct: bool,
        is_frozen: bool = False,
    ) -> str:
        class_name: str = node.name
        fields_and_constructor: str = self._calc_fields_and_constructor(
            fields_and_base_constructor_calls,
            constructor_sig,
            is_frozen,
        )
        base_classes: list[str] = self._calc_base_classes(node)
        if name_starts_with_underscore or self._d.is_main_file:
            full_methods: str = _calc_full_methods(methods)
            return _calc_final_str(
                class_name,
                fields_and_constructor + full_methods,
                is_struct,
                base_classes,
            )
        if len(methods) == 0:
            self._d.ret_h_file.append(
                _calc_final_str(
                    class_name, fields_and_constructor, is_struct, base_classes
                )
            )
            # Nothing goes in the cpp file in this case.
            return ""
        method_signatures: str = _calc_method_signatures(methods)
        method_impls: str = _calc_method_implementations(methods, class_name)
        self._d.ret_h_file.append(
            _calc_final_str(
                class_name,
                fields_and_constructor + method_signatures,
                is_struct,
                base_classes,
            )
        )
        return method_impls

    def _calc_base_classes(self, node: ast.ClassDef) -> list[str]:
        ret: list[str] = []
        for base in node.bases:
            ret.append(self._d.handle_expr(base))
        return ret

    def _calc_fields_and_constructor(
        self,
        fields: list[ClassField],
        constructor_sig: str,
        is_frozen: bool,
    ):
        if constructor_sig == "":
            # There can't be any fields if there is no constructor.
            return ""
        field_defs = _calc_field_definitions(fields, is_frozen)
        c_il: str = self._calc_constructor_initializer_list(fields)
        if c_il != "":
            c_il = ": " + c_il
        return f"{field_defs} {constructor_sig} {c_il}" + "{}"

    def _calc_constructor_initializer_list(
        self, fields_and_base_constructor_calls: list[ClassField]
    ) -> str:
        ret: list[str] = []
        for field in fields_and_base_constructor_calls:
            if field.ref:
                ret.append(f"{field.target_str}({ARG_PREFIX}{field.target_other_name})")
            else:
                self._d.add_inc(AngInc("utility"))
                ret.append(
                    f"{field.target_str}(std::move({ARG_PREFIX}{field.target_other_name}))"
                )
        return ", ".join(ret)


def _calc_field_definitions(fields: list[ClassField], is_frozen: bool) -> str:
    ret: list[str] = []
    const_str = "const " if is_frozen else ""
    for field in fields:
        ret.append(f"{const_str}{field.type_cpp}{field.ref} {field.target_str};")
    return " ".join(ret)


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
        sig_with_namespace = _add_namespace(method, class_name)
        ret.append(calc_fn_str_with_body(sig_with_namespace, method.body_str))
    return "\n\n".join(ret)


def _add_namespace(method: ClassMethod, class_name: str) -> str:
    m = method.fn_signature.find(method.name)
    assert m != -1, SHOULDNT_HAPPEN
    return method.fn_signature[:m] + class_name + "::" + method.fn_signature[m:]


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
