import ast
from dataclasses import dataclass

from ..util.check_primitive_type import is_primitive_type
from pypp_cli.do.transpile.transpile.y.d_types import PyImp

from ...deps import Deps
from .h_tuple import handle_tuple_inner_args
from ..mapping.subscript_value import lookup_cpp_subscript_value_type


@dataclass(frozen=True, slots=True)
class SubscriptHandler:
    _d: Deps

    def handle(self, node: ast.Subscript) -> str:
        value_cpp_str = self._d.handle_expr(node.value)
        if value_cpp_str == "Ref" and self._d.is_imported(PyImp("pypp_python", "Ref")):
            cpp_type: str = self._d.handle_expr(node.slice)
            if is_primitive_type(cpp_type, self._d):
                self._d.value_err(
                    "Wrapping a primitive type in `Ref[]` is not supported",
                    node,
                )
            return f"&{cpp_type}"

        if value_cpp_str == "pypp::PyDefaultDict":
            if not isinstance(node.slice, ast.Tuple):
                self._d.value_err(
                    "defaultdict must be called as defaultdict[KeyType, ValueType]",
                    node,
                )
            if not len(node.slice.elts) == 2:
                self._d.value_err("2 types expected when calling defaultdict", node)
        if isinstance(node.slice, ast.Tuple):
            slice_cpp_str = handle_tuple_inner_args(node.slice, self._d)
        else:
            slice_cpp_str: str = self._d.handle_expr(node.slice)
        v1, v2 = lookup_cpp_subscript_value_type(value_cpp_str, self._d)
        return v1 + slice_cpp_str + v2
