import ast

from pypp_cli.src.transpilers.other.transpiler.deps import Deps
from dataclasses import dataclass

from ..handle_other.exception_handler import ExceptionHandlersHandler


@dataclass(frozen=True, slots=True)
class TryHandler:
    _d: Deps
    exception_handler: ExceptionHandlersHandler

    def handle(self, node: ast.Try) -> str:
        if len(node.orelse) != 0:
            self._d.value_err_no_ast("else not supported for try...except statement")
        if len(node.finalbody) != 0:
            self._d.value_err_no_ast("finally not supported for try...except statement")
        body_str: str = self._d.handle_stmts(node.body)
        self._d.inside_except_block = True
        exception_handlers_str: str = self.exception_handler.handle(node.handlers)
        self._d.inside_except_block = False
        return "try " + "{" + body_str + "} " + exception_handlers_str
