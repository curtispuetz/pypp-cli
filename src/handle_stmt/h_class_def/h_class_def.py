import ast

from src.handle_stmt.h_class_def.for_class.for_class import handle_class_def_for_class
from src.handle_stmt.h_class_def.for_dataclasses.for_dataclasses import (
    handle_class_def_for_dataclass,
)
from src.util.ret_imports import RetImports


def handle_class_def(
    node: ast.ClassDef,
    ret_imports: RetImports,
    ret_h_file: list[str],
    handle_stmt,
    handle_expr,
) -> str:
    # This only handles a dataclass right now.
    _do_common_assertions(node)
    if len(node.decorator_list) == 1:
        is_frozen: bool = _do_dataclass_assertions(node)
        return handle_class_def_for_dataclass(
            node, ret_imports, ret_h_file, handle_stmt, handle_expr, is_frozen
        )
    return handle_class_def_for_class(
        node, ret_imports, ret_h_file, handle_stmt, handle_expr
    )


def _do_common_assertions(node: ast.ClassDef) -> None:
    assert len(node.type_params) == 0, "type parameters for classes are not supported"
    assert len(node.keywords) == 0, "keywords for classes are not supported"


def _do_dataclass_assertions(node: ast.ClassDef) -> bool:
    # This only handles a dataclass right now.
    dataclass_decorator = node.decorator_list[0]
    is_frozen: bool = False
    if isinstance(dataclass_decorator, ast.Call):
        assert len(dataclass_decorator.args) == 0, (
            "only keyword args for dataclass are supported"
        )
        is_frozen = _check_dataclass_keywords(dataclass_decorator.keywords)
    else:
        assert isinstance(dataclass_decorator, ast.Name), (
            "args for dataclass decorator are not supported"
        )
        assert dataclass_decorator.id == "dataclass", (
            "only dataclass decorator is supported"
        )
    return is_frozen


def _check_dataclass_keywords(nodes: list[ast.keyword]) -> bool:
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
