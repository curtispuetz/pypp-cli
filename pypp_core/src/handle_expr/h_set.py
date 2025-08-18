import ast

from pypp_core.src.d_types import QInc
from pypp_core.src.deps import Deps


def handle_set(
    node: ast.Set,
    d: Deps,
    include_in_header: bool,
) -> str:
    d.add_inc(QInc("py_set.h"), include_in_header)
    return "PySet({" + d.handle_exprs(node.elts, include_in_header) + "})"
