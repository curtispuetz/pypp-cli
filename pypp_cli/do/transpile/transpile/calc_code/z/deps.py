from __future__ import annotations
import ast
from dataclasses import dataclass
from pathlib import Path

from pypp_cli.do.transpile.transpile.z_i.d_types import (
    CppInclude,
    ModulePyImports,
    PySpecificImport,
)
from pypp_cli.do.transpile.transpile.z_i.maps.d_types import Maps
from pypp_cli.do.transpile.transpile.z_i.cpp_includes import CppIncludes
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .handlers.handle_expr.expr import ExprHandler
    from .handlers.handle_stmt.h_ann_assign.h_ann_assign import AnnAssignHandler
    from .handlers.handle_stmt.h_type_alias import TypeAliasHandler
    from .handlers.handle_stmt.stmt import StmtHandler


@dataclass
class Deps:
    file_path: Path
    cpp_includes: CppIncludes
    ret_h_file: list[str]
    maps: Maps
    _module_py_imports: ModulePyImports
    namespaces: dict[str, str]
    _include_in_header: bool = False
    inside_except_block: bool = False
    is_main_file: bool = False

    def set_expr_handler(self, expr_handler: "ExprHandler"):
        self._expr_handler = expr_handler

    def set_stmt_handler(self, stmt_handler: "StmtHandler"):
        self._stmt_handler = stmt_handler

    def set_ann_assign_handler(self, handler: "AnnAssignHandler"):
        self._ann_assign_handler = handler

    def set_type_alias_handler(self, handler: "TypeAliasHandler"):
        self._type_alias_handler = handler

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
            ret.append(self._stmt_handler.handle(node))
        return " ".join(ret)

    def handle_stmts_for_module(self, stmts: list[ast.stmt]) -> str:
        ret: list[str] = []
        for node in stmts:
            if isinstance(node, ast.AnnAssign):
                ret.append(self._ann_assign_handler.handle(node, True))
            elif isinstance(node, ast.TypeAlias):
                ret.append(self._type_alias_handler.handle(node, True))
            else:
                ret.append(self._stmt_handler.handle(node))
        return " ".join(ret)

    def add_inc(self, inc: CppInclude):
        self.cpp_includes.add_inc(inc, self._include_in_header)

    def add_incs(self, incs: list[CppInclude]):
        for inc in incs:
            self.add_inc(inc)

    def is_imported(self, imp: PySpecificImport) -> bool:
        return self._module_py_imports.is_imported(imp)

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
