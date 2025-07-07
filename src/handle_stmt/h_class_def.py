import ast
from dataclasses import dataclass

from src.d_types import AngInc
from src.util.ret_imports import RetImports, add_inc
from src.util.util import calc_ref_str


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
    is_frozen: bool = False
    if isinstance(dataclass_decorator, ast.Call):
        assert len(dataclass_decorator.args) == 0, (
            "only keyword args for dataclass are supported"
        )
        is_frozen = _handle_dataclass_keywords(dataclass_decorator.keywords)
    else:
        assert isinstance(dataclass_decorator, ast.Name), (
            "args for dataclass decorator are not supported"
        )
        assert dataclass_decorator.id == "dataclass", (
            "only dataclass decorator is supported"
        )
    class_name: str = node.name
    name_doesnt_start_with_underscore: bool = not class_name.startswith("_")
    fields: list[_DataClassField] = _calc_fields(
        node, ret_imports, handle_expr, name_doesnt_start_with_underscore
    )
    field_defs = _calc_field_definitions(fields, is_frozen)
    c_sig: str = _calc_constructor_signature(class_name, fields)
    c_il: str = _calc_constructor_initializer_list(
        fields, ret_imports, name_doesnt_start_with_underscore
    )
    result: str = (
        f"struct {class_name}" + "{" + f"{field_defs} {c_sig} : {c_il}" + "{}" + "};"
    )
    if name_doesnt_start_with_underscore:
        ret_h_file.append(result)
        # Nothing goes in the cpp file.
        return ""
    else:
        return result


def _calc_constructor_signature(class_name: str, fields: list[_DataClassField]) -> str:
    ret: list[str] = []
    for field in fields:
        ret.append(f"{field.type_cpp}{field.ref} {ARG_PREFIX}{field.target_str}")
    return class_name + "(" + ", ".join(ret) + ")"


def _calc_constructor_initializer_list(
    fields: list[_DataClassField], ret_imports, name_doesnt_start_with_underscore: bool
) -> str:
    ret: list[str] = []
    for field in fields:
        if field.ref:
            ret.append(f"{field.target_str}({ARG_PREFIX}{field.target_str})")
        else:
            # TODO now: add the utility include for std::move
            add_inc(
                ret_imports,
                AngInc("utility"),
                in_header=name_doesnt_start_with_underscore,
            )
            ret.append(f"{field.target_str}(std::move({ARG_PREFIX}{field.target_str}))")
    return ", ".join(ret)


def _calc_field_definitions(fields: list[_DataClassField], is_frozen: bool) -> str:
    ret: list[str] = []
    const_str = "const " if is_frozen else ""
    for field in fields:
        ret.append(f"{const_str}{field.type_cpp}{field.ref} {field.target_str};")
    return " ".join(ret)


def _calc_fields(
    node: ast.ClassDef,
    ret_imports: RetImports,
    handle_expr,
    name_doesnt_start_with_underscore: bool,
) -> list[_DataClassField]:
    fields: list[_DataClassField] = []
    for item in node.body:
        assert isinstance(item, ast.AnnAssign), (
            "only AnnAssign in class body is supported"
        )
        fields.append(
            _handle_ann_assign_for_dataclass(
                item, ret_imports, handle_expr, name_doesnt_start_with_underscore
            )
        )
    return fields


def _handle_dataclass_keywords(nodes: list[ast.keyword]) -> bool:
    assert len(nodes) <= 2, "more than 2 args for dataclass decorator are not supported"
    frozen: bool = False
    for node in nodes:
        if node.arg == "frozen":
            assert isinstance(node.value, ast.Constant), "frozen must be a constant"
            assert isinstance(node.value.value, bool), "frozen must be a boolean"
            frozen = node.value.value
        elif node.arg != "slots":
            # slots is just ignored.
            raise NotImplementedError(f"unsupported dataclass keyword: {node.arg}")
    return frozen


def _handle_ann_assign_for_dataclass(
    node: ast.AnnAssign,
    ret_imports: RetImports,
    handle_expr,
    name_doesnt_start_with_underscore: bool,
) -> _DataClassField:
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
    ref, type_cpp = calc_ref_str(type_cpp)

    return _DataClassField(type_cpp, target_str, ref)
