import ast
from pypp_cli.do.transpile.transpile.handle.node import Deps
from .for_configclass import ConfigClassHandler
from .for_dataclasses.for_dataclasses import DataclassHandler
from .for_exception import ExceptionClassHandler
from dataclasses import dataclass
from .for_interface import InterfaceHandler


@dataclass(frozen=True, slots=True)
class ClassDefHandler:
    _d: Deps
    _config_class_handler: ConfigClassHandler
    _exception_class_handler: ExceptionClassHandler
    _dataclass_handler: DataclassHandler
    _interface_handler: InterfaceHandler

    def handle(self, node: ast.ClassDef) -> str:
        self._do_common_assertions(node)
        if len(node.decorator_list) > 1:
            self._d.value_err_class_name_no_ast(
                "multiple class decorators are not supported", node.name
            )
        if len(node.decorator_list) == 1:
            decorator_name = self._get_decorator_name(node)
            if decorator_name == "dataclass":
                is_frozen: bool = self._do_dataclass_assertions(node)
                return self._dataclass_handler.handle(node, is_frozen)
            elif decorator_name == "configclass":  # configclass
                dtype = self._do_configclass_assertions(node)
                return self._config_class_handler.handle(node, dtype)
            elif decorator_name == "exception":
                return self._exception_class_handler.handle(node)
            self._d.value_err_no_ast("unsupported class decorator: " + decorator_name)

        if _is_interface_def(node):
            self._do_interface_assertions(node)
            # This is a struct, which is a special case of a class.
            # Note: structs are not supported yet.
            return self._interface_handler.handle(node)
        self._d.value_err_class_name_no_ast(
            "class definition without a @dataclass, @configclass, or @exception "
            "decorator, "
            "or not an interface definition (i.e. inheriting from ABC) is not "
            "supported",
            node.name,
        )

    def _do_common_assertions(self, node: ast.ClassDef) -> None:
        if len(node.type_params) != 0:
            raise self._d.value_err_class_name_no_ast(
                "type parameters for classes are not supported", node.name
            )
        if len(node.keywords) != 0:
            raise self._d.value_err_class_name_no_ast(
                "keywords for classes are not supported", node.name
            )

    def _get_decorator_name(self, node: ast.ClassDef) -> str:
        decorator = node.decorator_list[0]
        if isinstance(decorator, ast.Call):
            if not isinstance(decorator.func, ast.Name):
                self._d.value_err_class_name(
                    "unsupported decorator", node.name, decorator
                )
            if decorator.func.id not in {"dataclass", "configclass"}:
                self._d.value_err_class_name(
                    "unsupported decorator", node.name, decorator
                )
            if len(decorator.args) != 0:
                self._d.value_err_class_name(
                    "only keyword args for class decorators are supported",
                    node.name,
                    decorator,
                )
            return decorator.func.id
        else:
            if not isinstance(decorator, ast.Name):
                self._d.value_err_class_name(
                    "something wrong with class decorator", node.name, decorator
                )
            return decorator.id

    def _do_configclass_assertions(self, node: ast.ClassDef) -> ast.expr | None:
        if len(node.bases) != 0:
            self._d.value_err_class_name_no_ast(
                "inheritance for configclass is not supported", node.name
            )
        decorator = node.decorator_list[0]
        if isinstance(decorator, ast.Call):
            keywords: list[ast.keyword] = decorator.keywords
            if len(keywords) != 1:
                self._d.value_err_class_name(
                    "multiple keyword args for configclass decorator is not supported",
                    node.name,
                    decorator,
                )
            if keywords[0].arg != "dtype":
                self._d.value_err_class_name(
                    "only 'dtype' keyword arg for configclass decorator is supported",
                    node.name,
                    keywords[0],
                )
            return keywords[0].value
        return None

    def _do_dataclass_assertions(self, node: ast.ClassDef) -> bool:
        decorator = node.decorator_list[0]
        is_frozen: bool = False
        if isinstance(decorator, ast.Call):
            is_frozen = self._check_dataclass_keywords(decorator.keywords, node.name)
        return is_frozen

    def _check_dataclass_keywords(
        self, nodes: list[ast.keyword], class_name: str
    ) -> bool:
        if len(nodes) > 2:
            self._d.value_err_class_name_no_ast(
                "More than 2 keyword args for dataclass decorator are supported",
                class_name,
            )
        frozen: bool = False
        for node in nodes:
            if node.arg == "frozen":
                r: bool | None = _calc_frozen(node)
                if r is None:
                    self._d.value_err_class_name(
                        "'frozen' keyword for dataclass decorator must be a boolean",
                        class_name,
                        node,
                    )
                frozen = r
            elif node.arg != "slots":
                # slots is just ignored.
                self._d.value_err_class_name(
                    f"unsupported dataclass keyword: {node.arg}", class_name, node
                )
        return frozen

    def _do_interface_assertions(self, node: ast.ClassDef) -> None:
        # assert that only methods/functions are defined in node.body and that each of
        # them has an 'abstractmethod' decorator
        for item in node.body:
            if not isinstance(item, ast.FunctionDef):
                self._d.value_err_class_name(
                    "only methods are supported in interface definitions",
                    node.name,
                    item,
                )
            if len(item.decorator_list) != 1:
                self._d.value_err_class_name_no_ast(
                    "methods in interface definitions must have exactly one decorator",
                    node.name,
                )
            decorator = item.decorator_list[0]
            if not (
                isinstance(decorator, ast.Name) and decorator.id == "abstractmethod"
            ):
                self._d.value_err_class_name(
                    "only 'abstractmethod' decorator is supported for methods in "
                    "interface definitions",
                    node.name,
                    decorator,
                )


def _is_interface_def(node: ast.ClassDef) -> bool:
    if len(node.bases) != 1:
        return False
    base = node.bases[0]
    return isinstance(base, ast.Name) and base.id == "ABC"


def _calc_frozen(node: ast.keyword) -> bool | None:
    if not isinstance(node.value, ast.Constant):
        return None
    if not isinstance(node.value.value, bool):
        return None
    return node.value.value
