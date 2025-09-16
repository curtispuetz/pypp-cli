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


@dataclass
class Deps:
    file_path: Path
    cpp_includes: CppIncludes
    ret_h_file: list[str]
    maps: Maps
    _py_imports: PyImports
    _handle_stmt: Callable[[ast.stmt, "Deps"], str]
    _handle_ann_assign: Callable[[ast.AnnAssign, "Deps", bool], str]
    _handle_type_alias: Callable[[ast.TypeAlias, "Deps", bool], str]
    user_namespace: set[str]
    _include_in_header: bool = False
    inside_except_block: bool = False
    is_main_file: bool = False

    def set_expr_handler(self, expr_handler: "ExprHandler"):
        self._expr_handler = expr_handler

    def set_inc_in_h(self, include: bool):
        self._include_in_header = include

    def handle_expr(self, node: ast.expr) -> str:
        return self._expr_handler.handle(node)

    def handle_exprs(self, exprs: list[ast.expr], join_str: str = ", ") -> str:
        ret: list[str] = []
        for node in exprs:
            ret.append(self.handle_expr(node))
        return join_str.join(ret)

    def handle_stmts(self, stmts: list[ast.stmt]) -> str:
        ret: list[str] = []
        for node in stmts:
            ret.append(self._handle_stmt(node, self))
        return " ".join(ret)

    def handle_stmts_for_module(self, stmts: list[ast.stmt]) -> str:
        ret: list[str] = []
        for node in stmts:
            if isinstance(node, ast.AnnAssign):
                ret.append(self._handle_ann_assign(node, self, True))
            elif isinstance(node, ast.TypeAlias):
                ret.append(self._handle_type_alias(node, self, True))
            else:
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
            f"{msg} \n\nThe problem code "
            f"(AST format https://docs.python.org/3/library/ast.html):"
            f"\n{ast.dump(ast_node, indent=4)}"
            f"\n\nOriginating from file:\n{self.file_path}"
        )

    def value_err_no_ast(self, msg: str):
        raise ValueError(f"{msg}\n\nOriginating from file:\n{self.file_path}")

    def value_err_class_name(self, msg: str, class_name: str, ast_node):
        raise ValueError(
            f"{msg}. Problem class: '{class_name}'\n\n"
            f"The problem code "
            f"(AST format https://docs.python.org/3/library/ast.html):"
            f"\n{ast.dump(ast_node, indent=4)}"
            f"\n\nOriginating from file:\n{self.file_path}"
        )

    def value_err_class_name_no_ast(self, msg: str, class_name: str):
        raise ValueError(
            f"{msg}. Problem class: '{class_name}'\n\n"
            f"Originating from file:\n{self.file_path}"
        )
