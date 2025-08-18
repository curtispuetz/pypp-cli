import ast
from dataclasses import dataclass
from typing import Callable

from pypp_core.src.d_types import CppInclude, PyImports, PySpecificImport, is_imported
from pypp_core.src.mapping.maps.maps import Maps
from pypp_core.src.util.ret_imports import RetImports, add_inc


@dataclass(frozen=True, slots=True)
class Deps:
    ret_imports: RetImports
    ret_h_file: list[str]
    py_imports: PyImports
    maps: Maps
    handle_expr_fn: Callable[[ast.expr, "Deps", bool, bool], str]
    handle_stmt: Callable[[ast.stmt, "Deps"], str]

    def handle_expr(
        self,
        node: ast.expr,
        include_in_header: bool = False,
        skip_cpp_lookup: bool = False,
    ) -> str:
        return self.handle_expr_fn(node, self, include_in_header, skip_cpp_lookup)

    def handle_exprs(
        self,
        exprs: list[ast.expr],
        include_in_header: bool = False,
    ):
        ret: list[str] = []
        for node in exprs:
            ret.append(self.handle_expr(node, include_in_header))
        return ", ".join(ret)  # Note: is it always going to join like this?

    def handle_stmts(self, stmts: list[ast.stmt]) -> str:
        ret: list[str] = []
        for node in stmts:
            ret.append(self.handle_stmt(node, self))
        return " ".join(ret)

    def add_inc(self, inc: CppInclude, in_header: bool = False):
        add_inc(self.ret_imports, inc, in_header)

    def is_imported(self, imp: PySpecificImport) -> bool:
        return is_imported(self.py_imports, imp)
