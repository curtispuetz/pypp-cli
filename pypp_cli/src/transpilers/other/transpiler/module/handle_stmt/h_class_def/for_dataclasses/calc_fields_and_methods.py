import ast
from pypp_cli.src.transpilers.other.transpiler.deps import Deps
from ...h_class_def.util import (
    ClassMethod,
    ClassField,
    MethodCalculator,
    calc_class_field,
)
from pypp_cli.src.transpilers.other.transpiler.module.mapping.cpp_type import (
    lookup_cpp_type,
)
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class FieldsAndMethodsCalculator:
    _d: Deps
    _method_calculator: MethodCalculator

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
        type_str = lookup_cpp_type(type_cpp, self._d)
        return calc_class_field(type_str, target_str, target_str)
