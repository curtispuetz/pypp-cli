import ast
from pypp_cli.do.transpile.transpile.handle.z.deps import Deps
from pypp_cli.do.transpile.transpile.handle.z.handlers.mapping.cpp_type import (
    CppTypeCalculator,
)
from .class_field_calculator import calc_class_field
from .method_calculator import ClassMethod, MethodCalculator
from .class_field_calculator import (
    ClassField,
)
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class FieldsAndMethodsCalculator:
    _d: Deps
    _method_calculator: MethodCalculator
    _cpp_type_calculator: CppTypeCalculator

    def calc(
        self, node: ast.ClassDef, is_def_in_header: bool
    ) -> tuple[list[ClassField], list[ClassMethod]]:
        fields: list[ClassField] = []
        methods: list[ClassMethod] = []
        for item in node.body:
            if isinstance(item, ast.AnnAssign):
                fields.append(self._calc_field(item))
            elif isinstance(item, ast.FunctionDef):
                methods.append(
                    self._method_calculator.calc(
                        item,
                        is_def_in_header,
                    )
                )
            else:
                self._d.value_err(
                    f"only field definitions and methods are supported in a dataclass. "
                    f"Problem class: {node.name}",
                    item,
                )
        return fields, methods

    def _calc_field(self, node: ast.AnnAssign) -> ClassField:
        if node.value is not None:
            self._d.value_err(
                "default values for dataclass attributes are not supported", node
            )
        type_cpp: str = self._d.handle_expr(node.annotation)
        target_str: str = self._d.handle_expr(node.target)
        type_str = self._cpp_type_calculator.calc(type_cpp)
        return calc_class_field(type_str, target_str, target_str)
