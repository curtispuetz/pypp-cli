import ast
from dataclasses import dataclass
from pathlib import Path
from typing import Callable

from pypp_cli.src.transpilers.other.transpiler.d_types import (
    CppInclude,
    PyImports,
    PySpecificImport,
    is_imported,
)
from pypp_cli.src.transpilers.other.transpiler.maps.maps import Maps
from pypp_cli.src.transpilers.other.transpiler.cpp_includes import CppIncludes


@dataclass(slots=True)
class Deps:
    file_path: Path
    cpp_includes: CppIncludes
    ret_h_file: list[str]
    maps: Maps
    _py_imports: PyImports
    _handle_expr_fn: Callable[[ast.expr, "Deps"], str]
    _handle_stmt: Callable[[ast.stmt, "Deps"], str]
    user_namespace: set[str]
    _include_in_header: bool = False

    def set_inc_in_h(self, include: bool):
        self._include_in_header = include

    def handle_expr(self, node: ast.expr) -> str:
        return self._handle_expr_fn(node, self)

    def handle_exprs(self, exprs: list[ast.expr]):
        ret: list[str] = []
        for node in exprs:
            ret.append(self.handle_expr(node))
        return ", ".join(ret)  # Note: is it always going to join like this?

    def handle_stmts(self, stmts: list[ast.stmt]) -> str:
        ret: list[str] = []
        for node in stmts:
            ret.append(self._handle_stmt(node, self))
        return " ".join(ret)

    def add_inc(self, inc: CppInclude):
        self.cpp_includes.add_inc(inc, self._include_in_header)

    def add_incs(self, incs: list[CppInclude]):
        for inc in incs:
            self.add_inc(inc)

    def is_imported(self, imp: PySpecificImport) -> bool:
        return is_imported(self._py_imports, imp)

    def value_err(self, msg: str, ast_node):
        raise ValueError(
            f"{msg} \n The problem AST node:\n{ast.dump(ast_node, indent=4)}"
            f"\nIn file:\n{self.file_path}"
        )

    def value_err_no_ast(self, msg: str):
        raise ValueError(f"{msg} \nIn file:\n{self.file_path}")

    def value_err_class_name(self, msg: str, class_name: str, ast_node):
        raise ValueError(
            f"{msg}. Problem class: {class_name}\n "
            f"The problem AST node:\n{ast.dump(ast_node, indent=4)}"
            f"\nIn file:\n{self.file_path}"
        )

    def value_err_class_name_no_ast(self, msg: str, class_name: str):
        raise ValueError(
            f"{msg}. Problem class: {class_name}\nIn file:\n{self.file_path}"
        )
