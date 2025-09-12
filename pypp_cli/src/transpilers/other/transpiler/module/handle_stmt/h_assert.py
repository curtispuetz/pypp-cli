import ast

from pypp_cli.src.transpilers.other.transpiler.d_types import QInc
from pypp_cli.src.transpilers.other.transpiler.deps import Deps


def handle_assert(node: ast.Assert, d: Deps) -> str:
    d.add_inc(QInc("pypp_assert.h"))
    test_str = d.handle_expr(node.test)
    if node.msg is not None:
        msg_str = d.handle_expr(node.msg)
    else:
        msg_str = 'pypp::PyStr("")'
    return f"pypp::assert({test_str}, {msg_str});"
