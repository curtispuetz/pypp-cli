import ast

from compy_cli.src.transpiler.deps import Deps
from compy_cli.src.transpiler.handle_stmt.h_class_def.for_class.for_class import (
    handle_class_def_for_class,
)
from compy_cli.src.transpiler.handle_stmt.h_class_def.for_configclass.for_configclass import (  # noqa: E501
    handle_class_def_for_configclass,
)
from compy_cli.src.transpiler.handle_stmt.h_class_def.for_dataclasses.for_dataclasses import (  # noqa: E501
    handle_class_def_for_dataclass,
)
from compy_cli.src.transpiler.handle_stmt.h_class_def.for_exception import (
    handle_class_def_for_exception,
)
from compy_cli.src.transpiler.handle_stmt.h_class_def.for_interface.for_interface import (  # noqa: E501
    handle_class_def_for_interface,
)


def handle_class_def(node: ast.ClassDef, d: Deps) -> str:
    _do_common_assertions(node)
    if len(node.decorator_list) == 1:
        decorator_name = _get_decorator_name(node)
        if decorator_name == "dataclass":
            is_frozen: bool = _do_dataclass_assertions(node)
            return handle_class_def_for_dataclass(node, d, is_frozen)
        elif decorator_name == "configclass":  # configclass
            dtype = _do_configclass_assertions(node)
            return handle_class_def_for_configclass(node, d, dtype)
        elif decorator_name == "exception":
            return handle_class_def_for_exception(node, d)
        raise ValueError("unsupported class decorator: " + decorator_name)

    if _is_interface_def(node):
        _do_interface_assertions(node)
        # This is a struct, which is a special case of a class.
        # Note: structs are not supported yet.
        return handle_class_def_for_interface(node, d)
    return handle_class_def_for_class(node, d)


def _is_interface_def(node: ast.ClassDef) -> bool:
    if len(node.bases) != 1:
        return False
    base = node.bases[0]
    return isinstance(base, ast.Name) and base.id == "ABC"


def _do_common_assertions(node: ast.ClassDef) -> None:
    assert len(node.type_params) == 0, "type parameters for classes are not supported"
    assert len(node.keywords) == 0, "keywords for classes are not supported"


def _get_decorator_name(node: ast.ClassDef) -> str:
    decorator = node.decorator_list[0]
    if isinstance(decorator, ast.Call):
        assert isinstance(decorator.func, ast.Name), (
            "only @dataclass and @configclass decorators supported for classes"
        )
        if decorator.func.id not in {"dataclass", "configclass"}:
            raise Exception(
                "only @dataclass and @configclass decorators supported for classes"
            )
        assert len(decorator.args) == 0, (
            "only keyword args for class decorators are supported"
        )
        return decorator.func.id
    else:
        assert isinstance(decorator, ast.Name), "something wrong with class decorator"
        return decorator.id


def _do_configclass_assertions(node: ast.ClassDef) -> ast.expr | None:
    assert len(node.bases) == 0, "inheritance for configclass is not supported"
    decorator = node.decorator_list[0]
    if isinstance(decorator, ast.Call):
        keywords: list[ast.keyword] = decorator.keywords
        error_str: str = (
            "only 'dtype' keyword arg for configclass decorator is supported"
        )
        assert len(keywords) == 1, error_str
        assert keywords[0].arg == "dtype", error_str
        return keywords[0].value
    return None


def _do_dataclass_assertions(node: ast.ClassDef) -> bool:
    assert len(node.bases) == 0, "inheritance for dataclass is not supported"
    decorator = node.decorator_list[0]
    is_frozen: bool = False
    if isinstance(decorator, ast.Call):
        is_frozen = _check_dataclass_keywords(decorator.keywords)
    return is_frozen


def _check_dataclass_keywords(nodes: list[ast.keyword]) -> bool:
    assert len(nodes) <= 2, (
        "only 'frozen' and 'slots' keyword args for dataclass decorator are supported"
    )
    frozen: bool = False
    for node in nodes:
        if node.arg == "frozen":
            assert isinstance(node.value, ast.Constant), "frozen must be a boolean"
            assert isinstance(node.value.value, bool), "frozen must be a boolean"
            frozen = node.value.value
        elif node.arg != "slots":
            # slots is just ignored.
            raise NotImplementedError(f"unsupported dataclass keyword: {node.arg}")
    return frozen


def _do_interface_assertions(node: ast.ClassDef) -> None:
    # assert that only methods/functions are defined in node.body and that each of them
    # has an 'abstractmethod' decorator
    for item in node.body:
        assert isinstance(item, ast.FunctionDef), (
            f"only methods are supported in interface definitions, got "
            f"{type(item).__name__}"
        )
        if len(item.decorator_list) == 1:
            decorator = item.decorator_list[0]
            assert (
                isinstance(decorator, ast.Name) and decorator.id == "abstractmethod"
            ), (
                f"method {item.name} in interface {node.name} must be decorated only "
                f"with @abstractmethod"
            )
