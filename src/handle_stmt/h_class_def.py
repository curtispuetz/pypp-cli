import ast
from dataclasses import dataclass

from src.d_types import AngInc
from src.handle_expr.h_name import handle_name
from src.util.ret_imports import RetImports, add_inc
from src.util.util import calc_ref_str

# TODO: check about supporting frozen dataclasses and maybe ignoring slots == True.
#  note: this can be done by making the struct member variables const.
# TODO: support dataclasses only in the CPP file and not the header if it starts with
#  an underscore.

@dataclass(frozen=True, slots=True)
class _DataClassField:
    type_cpp: str
    target_str: str
    ref: str


ARG_PREFIX = "a_"


def handle_class_def(
    node: ast.ClassDef,
    ret_imports: RetImports,
    ret_h_file: list[str],
    handle_stmt,
    handle_expr,
) -> str:
    # This only handles a dataclass right now.
    assert len(node.decorator_list) == 1, (
        "only dataclass decorator for classes are supported"
    )
    assert len(node.type_params) == 0, "type parameters for classes are not supported"
    assert len(node.bases) == 0, "base classes are not supported"
    assert len(node.keywords) == 0, "keywords for class definition are not supported"
    dataclass_decorator = node.decorator_list[0]
    assert isinstance(dataclass_decorator, ast.Name), (
        "args for dataclass decorator are not supported"
    )
    d = handle_name(dataclass_decorator, ret_imports, True, False)
    assert d == "dataclass", "only dataclass decorator is supported"
    fields: list[_DataClassField] = _calc_fields(node, ret_imports, handle_expr)
    field_defs = _calc_field_definitions(fields)
    class_name: str = node.name
    c_sig: str = _calc_constructor_signature(class_name, fields)
    c_il: str = _calc_constructor_initializer_list(fields, ret_imports)
    ret_h_file.append(
        f"struct {class_name}" + "{" + f"{field_defs} {c_sig} : {c_il}" + "{}" + "};"
    )
    # Nothing goes in the cpp file.
    return ""


def _calc_constructor_signature(class_name: str, fields: list[_DataClassField]) -> str:
    ret: list[str] = []
    for field in fields:
        ret.append(f"{field.type_cpp}{field.ref} {ARG_PREFIX}{field.target_str}")
    return class_name + "(" + ", ".join(ret) + ")"


def _calc_constructor_initializer_list(
    fields: list[_DataClassField], ret_imports
) -> str:
    ret: list[str] = []
    for field in fields:
        if field.ref:
            ret.append(f"{field.target_str}({ARG_PREFIX}{field.target_str})")
        else:
            # TODO now: add the utility include for std::move
            add_inc(ret_imports, AngInc("utility"), in_header=True)
            ret.append(f"{field.target_str}(std::move({ARG_PREFIX}{field.target_str}))")
    return ", ".join(ret)


def _calc_field_definitions(fields: list[_DataClassField]) -> str:
    ret: list[str] = []
    for field in fields:
        ret.append(f"{field.type_cpp}{field.ref} {field.target_str};")
    return " ".join(ret)


def _calc_fields(node: ast.ClassDef, ret_imports: RetImports, handle_expr):
    fields: list[_DataClassField] = []
    for item in node.body:
        assert isinstance(item, ast.AnnAssign), (
            "only AnnAssign in class body is supported"
        )
        fields.append(_handle_ann_assign_for_dataclass(item, ret_imports, handle_expr))
    return fields


def _handle_ann_assign_for_dataclass(
    node: ast.AnnAssign, ret_imports: RetImports, handle_expr
) -> _DataClassField:
    assert node.value is None, (
        "default values for dataclass attributes are not supported"
    )
    type_cpp: str = handle_expr(node.annotation, ret_imports, include_in_header=True)
    target_str: str = handle_expr(node.target, ret_imports, include_in_header=True)
    ref, type_cpp = calc_ref_str(type_cpp)

    return _DataClassField(type_cpp, target_str, ref)
