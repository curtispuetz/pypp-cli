import ast

from pypp_cli.src.transpilers.other.transpiler.deps import Deps
from pypp_cli.src.transpilers.other.transpiler.module.handle_other.exception_handler import (  # noqa: E501
    handle_exception_handlers,
)

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class TryHandler:
    _d: Deps

    def handle(self, node: ast.Try) -> str:
        if len(node.orelse) != 0:
            self._d.value_err_no_ast("else not supported for try...except statement")
        if len(node.finalbody) != 0:
            self._d.value_err_no_ast("finally not supported for try...except statement")
        body_str: str = self._d.handle_stmts(node.body)
        self._d.inside_except_block = True
        exception_handlers_str: str = handle_exception_handlers(node.handlers, self._d)
        self._d.inside_except_block = False
        return "try " + "{" + body_str + "} " + exception_handlers_str
