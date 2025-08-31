import ast

from compy_cli.src.transpilers.other.transpiler.deps import Deps
from compy_cli.src.transpilers.other.module.handle_other.exception_handler import (
    handle_exception_handlers,
)


def handle_try(node: ast.Try, d: Deps):
    assert len(node.orelse) == 0, "else not supported for try...except"
    assert len(node.finalbody) == 0, "finally not supported for try...except"
    body_str: str = d.handle_stmts(node.body)
    exception_handlers_str: str = handle_exception_handlers(node.handlers, d)
    return "try " + "{" + body_str + "} " + exception_handlers_str
