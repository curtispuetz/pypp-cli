import ast
from dataclasses import dataclass

from pypp_cli.src.transpilers.other.transpiler.d_types import PySpecificImpFrom
from pypp_cli.src.transpilers.other.transpiler.deps import Deps
from pypp_cli.src.transpilers.other.transpiler.module.handle_expr.h_starred import (
    handle_call_with_starred_arg,
)
from pypp_cli.src.transpilers.other.transpiler.maps.d_types import (
    ToStringEntry,
    CustomMappingEntry,
    CustomMappingFromLibEntry,
    CustomMappingStartsWithEntry,
    CustomMappingStartsWithFromLibEntry,
    LeftAndRightEntry,
    ReplaceDotWithDoubleColonEntry,
)
from pypp_cli.src.transpilers.other.transpiler.module.mapping.util import (
    calc_string_fn,
    find_map_entry,
)
from pypp_cli.src.transpilers.other.transpiler.module.util.check_primitive_type import (
    is_primitive_type,
)


@dataclass(frozen=True, slots=True)
class CallHandler:
    _d: Deps

    def handle(self, node: ast.Call) -> str:
        if len(node.keywords) != 0:
            self._d.value_err("keywords for a call are not supported", node)
        caller_str: str = self._d.handle_expr(node.func)
        if caller_str == "Ref" and self._d.is_imported(
            PySpecificImpFrom("pypp_python", "Ref")
        ):
            if len(node.args) != 1:
                self._d.value_err("Ref() must have exactly one argument.", node)
            cpp_type: str = self._d.handle_expr(node.args[0])
            if is_primitive_type(cpp_type, self._d):
                self._d.value_err(
                    "Wrapping a primitive type in `Ref()` is not supported",
                    node,
                )
            return f"&{cpp_type}"
        for k, v in self._d.maps.call.items():
            e = find_map_entry(v, self._d)
            if e is None:
                continue
            if isinstance(e, ToStringEntry):
                if caller_str == k:
                    self._d.add_incs(e.includes)
                    return f"{e.to}({self._d.handle_exprs(node.args)})"
            elif isinstance(e, LeftAndRightEntry):
                if caller_str == k:
                    self._d.add_incs(e.includes)
                    return e.left + self._d.handle_exprs(node.args) + e.right
            elif isinstance(e, CustomMappingEntry):
                if caller_str == k:
                    self._d.add_incs(e.includes)
                    return e.mapping_fn(node, self._d)
            elif isinstance(e, CustomMappingFromLibEntry):
                if caller_str == k:
                    self._d.add_incs(e.includes)
                    return calc_string_fn(e)(node, self._d)
            elif isinstance(e, CustomMappingStartsWithEntry):
                if caller_str.startswith(k):
                    self._d.add_incs(e.includes)
                    return e.mapping_fn(node, self._d, caller_str)
            elif isinstance(e, CustomMappingStartsWithFromLibEntry):
                if caller_str.startswith(k):
                    self._d.add_incs(e.includes)
                    return calc_string_fn(e)(node, self._d, caller_str)
            elif isinstance(e, ReplaceDotWithDoubleColonEntry):
                if caller_str.startswith(k):
                    self._d.add_incs(e.includes)
                    caller_str = caller_str.replace(".", "::")
                    if e.add_pypp_namespace:
                        caller_str = "pypp::" + caller_str
                    return f"{caller_str}({self._d.handle_exprs(node.args)})"
        return f"{caller_str}({self._d.handle_exprs(node.args)})"


# TODO later: support starred arguments
def _handle_call_with_starred_arg(
    node: ast.Call, d: Deps, caller_str: str
) -> str | None:
    if len(node.args) == 1:
        first_arg = node.args[0]
        if isinstance(first_arg, ast.Starred):
            if len(node.args) != 1:
                d.value_err(
                    "Only one argument is allowed when using a starred argument.", node
                )
            return handle_call_with_starred_arg(first_arg, d, caller_str)
    return None
