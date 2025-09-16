import ast
from dataclasses import dataclass

from pypp_cli.src.transpilers.other.transpiler.deps import Deps
from pypp_cli.src.transpilers.other.transpiler.module.handle_expr.h_tuple import (
    handle_tuple_inner_args,
)
from pypp_cli.src.transpilers.other.transpiler.module.mapping.subscript_value import (
    lookup_cpp_subscript_value_type,
)


@dataclass(frozen=True, slots=True)
class SubscriptHandler:
    _d: Deps

    def handle(self, node: ast.Subscript) -> str:
        value_cpp_str = self._d.handle_expr(node.value)
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
