import ast

from src.d_types import QInc
from src.deps import Deps
from src.util.ret_imports import add_inc


def handle_assert(node: ast.Assert, d: Deps) -> str:
    add_inc(d.ret_imports, QInc("pypp_assert.h"))
    test_str = d.handle_expr(node.test)
    msg_str = 'PyStr("")'
    if node.msg is not None:
        # TODO: there is a problem here because I shouldn't be passing d.ret_h_file.
        msg_str = d.handle_expr(node.msg, d.ret_h_file)
    return f"assert({test_str}, {msg_str});"
