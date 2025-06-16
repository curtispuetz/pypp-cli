import ast

from src.handle_other.exception_handler import handle_exception_handlers
from src.d_types import CppInclude
from src.util.handle_lists import handle_stmts


def handle_try(
    node: ast.Try,
    ret_imports: set[CppInclude],
    ret_h_file: list[str],
    handle_stmt,
    handle_expr,
):
    assert len(node.orelse) == 0, "else not supported for try...except"
    assert len(node.finalbody) == 0, "finally not supported for try...except"
    body_str: str = handle_stmts(node.body, ret_imports, ret_h_file, handle_stmt)
    exception_handlers_str: str = handle_exception_handlers(
        node.handlers, ret_imports, ret_h_file, handle_stmt
    )
    return "try " + "{" + body_str + "} " + exception_handlers_str
