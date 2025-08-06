import ast

from src.d_types import QInc
from src.deps import Deps
from src.util.handle_lists import handle_exprs


def handle_set(
    node: ast.Set,
    d: Deps,
    include_in_header: bool,
) -> str:
    d.add_inc(QInc("py_set.h"), include_in_header)
    return "PySet({" + handle_exprs(node.elts, d, include_in_header) + "})"
