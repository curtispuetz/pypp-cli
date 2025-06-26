import ast

from src.d_types import AngInc, QInc
from src.util.ret_imports import RetImports, add_inc


def handle_assert(
    node: ast.Assert,
    ret_imports: RetImports,
    ret_h_file: list[str],
    handle_expr,
) -> str:
    add_inc(ret_imports, QInc("exceptions/stdexcept.h"))
    test_str = handle_expr(node.test, ret_imports, ret_h_file)
    msg_str = 'PyStr("")'
    if node.msg is not None:
        msg_str = handle_expr(node.msg, ret_imports, ret_h_file)
    return f"if (!({test_str}))" + "{" + f"throw PyppAssertionError({msg_str}.str());" + "}"