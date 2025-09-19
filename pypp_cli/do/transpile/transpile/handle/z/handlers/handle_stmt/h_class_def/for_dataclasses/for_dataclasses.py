import ast
from pypp_cli.do.transpile.transpile.handle.node import Deps
from .create_final_str import DataclassFinalStrCreator
from .calc_constructor_sig import calc_constructor_signature_for_dataclass
from dataclasses import dataclass
from .calc_fields_and_methods import FieldsAndMethodsCalculator


@dataclass(frozen=True, slots=True)
class DataclassHandler:
    _d: Deps
    _fields_and_methods_calculator: FieldsAndMethodsCalculator
    _dataclass_final_str_creator: DataclassFinalStrCreator

    def handle(self, node: ast.ClassDef, is_frozen: bool) -> str:
        is_def_in_header: bool = not self._d.is_main_file and not node.name.startswith(
            "_"
        )

        self._d.set_inc_in_h(is_def_in_header)
        fields, methods = self._fields_and_methods_calculator.calc(
            node, is_def_in_header
        )
        constructor_sig = calc_constructor_signature_for_dataclass(fields, node.name)
        ret = self._dataclass_final_str_creator.create(
            node,
            fields,
            methods,
            constructor_sig,
            node.name.startswith("_"),
            True,
            is_frozen,
        )
        self._d.set_inc_in_h(False)

        return ret
