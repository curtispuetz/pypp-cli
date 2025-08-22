import ast

from pypp_core.src.d_types import QInc
from pypp_core.src.deps import Deps


def handle_tuple_inner_args(node: ast.Tuple, d: Deps):
    return d.handle_exprs(node.elts)


def handle_tuple(node: ast.Tuple, d: Deps) -> str:
    d.add_inc(QInc("py_tuple.h"))
    # TODO: is this still good to have tuples always own its data?
    # I don't think it is right actually anymore.
    args_str: str = d.handle_exprs(node.elts)
    return f"PyTup({args_str})"
