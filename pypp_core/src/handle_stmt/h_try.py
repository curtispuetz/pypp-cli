import ast

from pypp_core.src.deps import Deps
from pypp_core.src.handle_other.exception_handler import handle_exception_handlers
from pypp_core.src.util.handle_lists import handle_stmts


def handle_try(node: ast.Try, d: Deps):
    assert len(node.orelse) == 0, "else not supported for try...except"
    assert len(node.finalbody) == 0, "finally not supported for try...except"
    body_str: str = handle_stmts(node.body, d)
    exception_handlers_str: str = handle_exception_handlers(node.handlers, d)
    return "try " + "{" + body_str + "} " + exception_handlers_str
