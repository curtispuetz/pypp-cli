import ast

from src.d_types import QInc
from src.deps import Deps


def handle_assert(node: ast.Assert, d: Deps) -> str:
    d.add_inc(QInc("pypp_assert.h"))
    test_str = d.handle_expr(node.test)
    msg_str = 'PyStr("")'
    if node.msg is not None:
        msg_str = d.handle_expr(node.msg)
    return f"assert({test_str}, {msg_str});"
