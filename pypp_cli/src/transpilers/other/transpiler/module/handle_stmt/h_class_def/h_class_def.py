import ast
from multiprocessing import Value

from pypp_cli.src.transpilers.other.transpiler.deps import Deps
from pypp_cli.src.transpilers.other.transpiler.module.handle_stmt.h_class_def.for_configclass.for_configclass import (  # noqa: E501
    handle_class_def_for_configclass,
)
from pypp_cli.src.transpilers.other.transpiler.module.handle_stmt.h_class_def.for_dataclasses.for_dataclasses import (  # noqa: E501
    handle_class_def_for_dataclass,
)
from pypp_cli.src.transpilers.other.transpiler.module.handle_stmt.h_class_def.for_exception import (  # noqa: E501
    handle_class_def_for_exception,
)
from pypp_cli.src.transpilers.other.transpiler.module.handle_stmt.h_class_def.for_interface.for_interface import (  # noqa: E501
    handle_class_def_for_interface,
)


def handle_class_def(node: ast.ClassDef, d: Deps) -> str:
    _do_common_assertions(node, d)
    if len(node.decorator_list) > 1:
        d.value_err_class_name_no_ast(
            "multiple class decorators are not supported", node.name
        )
    if len(node.decorator_list) == 1:
        decorator_name = _get_decorator_name(node, d)
        if decorator_name == "dataclass":
            is_frozen: bool = _do_dataclass_assertions(node, d)
            return handle_class_def_for_dataclass(node, d, is_frozen)
        elif decorator_name == "configclass":  # configclass
            dtype = _do_configclass_assertions(node, d)
            return handle_class_def_for_configclass(node, d, dtype)
        elif decorator_name == "exception":
            return handle_class_def_for_exception(node, d)
        d.value_err_no_ast("unsupported class decorator: " + decorator_name)

    if _is_interface_def(node):
        _do_interface_assertions(node, d)
        # This is a struct, which is a special case of a class.
        # Note: structs are not supported yet.
        return handle_class_def_for_interface(node, d)
    d.value_err_class_name_no_ast(
        "class definition without a @dataclass, @configclass, or @exception decorator, "
        "or not an interface definition (i.e. inheriting from ABC) is not supported",
        node.name,
    )


def _is_interface_def(node: ast.ClassDef) -> bool:
    if len(node.bases) != 1:
        return False
    base = node.bases[0]
    return isinstance(base, ast.Name) and base.id == "ABC"


def _do_common_assertions(node: ast.ClassDef, d: Deps) -> None:
    if len(node.type_params) != 0:
        raise d.value_err_class_name_no_ast(
            "type parameters for classes are not supported", node.name
        )
    if len(node.keywords) != 0:
        raise d.value_err_class_name_no_ast(
            "keywords for classes are not supported", node.name
        )


def _get_decorator_name(node: ast.ClassDef, d: Deps) -> str:
    decorator = node.decorator_list[0]
    if isinstance(decorator, ast.Call):
        if not isinstance(decorator.func, ast.Name):
            d.value_err_class_name("unsupported decorator", node.name, decorator)
        if decorator.func.id not in {"dataclass", "configclass"}:
            d.value_err_class_name("unsupported decorator", node.name, decorator)
        if len(decorator.args) != 0:
            d.value_err_class_name(
                "only keyword args for class decorators are supported",
                node.name,
                decorator,
            )
        return decorator.func.id
    else:
        if not isinstance(decorator, ast.Name):
            d.value_err_class_name(
                "something wrong with class decorator", node.name, decorator
            )
        return decorator.id


def _do_configclass_assertions(node: ast.ClassDef, d: Deps) -> ast.expr | None:
    if len(node.bases) != 0:
        d.value_err_class_name_no_ast(
            "inheritance for configclass is not supported", node.name
        )
    decorator = node.decorator_list[0]
    if isinstance(decorator, ast.Call):
        keywords: list[ast.keyword] = decorator.keywords
        if len(keywords) != 1:
            d.value_err_class_name(
                "multiple keyword args for configclass decorator is not supported",
                node.name,
                decorator,
            )
        if keywords[0].arg != "dtype":
            d.value_err_class_name(
                "only 'dtype' keyword arg for configclass decorator is supported",
                node.name,
                keywords[0],
            )
        return keywords[0].value
    return None


def _do_dataclass_assertions(node: ast.ClassDef, d: Deps) -> bool:
    decorator = node.decorator_list[0]
    is_frozen: bool = False
    if isinstance(decorator, ast.Call):
        is_frozen = _check_dataclass_keywords(decorator.keywords, node.name, d)
    return is_frozen


def _check_dataclass_keywords(
    nodes: list[ast.keyword], class_name: str, d: Deps
) -> bool:
    if len(nodes) > 2:
        d.value_err_class_name_no_ast(
            "More than 2 keyword args for dataclass decorator are supported",
            class_name,
        )
    frozen: bool = False
    for node in nodes:
        if node.arg == "frozen":
            r: bool | None = _calc_frozen(node)
            if r is None:
                d.value_err_class_name(
                    "'frozen' keyword for dataclass decorator must be a boolean",
                    class_name,
                    node,
                )
            frozen = r
        elif node.arg != "slots":
            # slots is just ignored.
            d.value_err_class_name(
                f"unsupported dataclass keyword: {node.arg}", class_name, node
            )
    return frozen


def _calc_frozen(node: ast.keyword) -> bool | None:
    if not isinstance(node.value, ast.Constant):
        return None
    if not isinstance(node.value.value, bool):
        return None
    return node.value.value


def _do_interface_assertions(node: ast.ClassDef, d: Deps) -> None:
    # assert that only methods/functions are defined in node.body and that each of them
    # has an 'abstractmethod' decorator
    for item in node.body:
        if not isinstance(item, ast.FunctionDef):
            d.value_err_class_name(
                "only methods are supported in interface definitions",
                node.name,
                item,
            )
        if len(item.decorator_list) != 1:
            d.value_err_class_name_no_ast(
                "methods in interface definitions must have exactly one decorator",
                node.name,
            )
        decorator = item.decorator_list[0]
        if not (isinstance(decorator, ast.Name) and decorator.id == "abstractmethod"):
            d.value_err_class_name(
                "only 'abstractmethod' decorator is supported for methods in "
                "interface definitions",
                node.name,
                decorator,
            )
